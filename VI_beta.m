function [ u, L ] = VI_beta( X,Y )
    % X is the input F_aspect, the aspect feature matrix
    % Y is the input S_aspect, the aspect rating
    % u is the mean of beta

    [n,d] = size(X);

    % Step 1: Set initial parameters
    e = n/2+1; % e is the new parameter in q distriution of lambda
    a = 1/2+10^(-16); % a is the new parameter in q distriution of alpha_j
    b = zeros(1,d); % b[j] is the parameter in q distribution of alpha_j
    var = 0.0001*eye(d);
    u = zeros(d,1);


    % Step 2.1 pre_calculate for q(beta), sum of XiYi, XiXi
    Sxx = zeros(d,d);
    Sxy = zeros(1,d);
    for i=1:n
        Sx = transpose(X(i,:))*X(i,:);
        Sxx = Sx+Sxx; % it is sum(xixi^T) to update var
        Sy = Y(i)*X(i,:);
        Sxy = Sxy+Sy; % it is (yixi) to update u
    end

    % Step 2.2 iteration
    E_a=zeros(1,d);
    lnb=zeros(1,d);
    L=zeros(1,80);

    for t=1:80
        % precalculate_2 for updating q(?)
        for i=1:n
            S3(i)=(Y(i)-X(i,:)*u)^2+X(i,:)*var*transpose(X(i,:));
            %It is sum[(Yi-xi^T*u)^2+Xi*var*Xi]
        end
        % -Update q(?)
        f=1/2*sum(S3)+1;
        E_nmbd=e/f;

        % -Update q(alpha_j), for iteration k=1,d
        for k=1:d
            b(k)=(u(k)*u(k))/2+var(k,k)+1e-10;
            E_a(k)=a/b(k);
            lnb(k)=log(b(k));
        end

        % Update q(beta)
        var=inv(diag(E_a)+E_nmbd*Sxx);
        u=E_nmbd*var*transpose(Sxy);

        % Calculate L
        S4=prod(diag(chol(var)));
        L(t)=log(S4)-e*log(f)-a*sum(lnb);
    end
end