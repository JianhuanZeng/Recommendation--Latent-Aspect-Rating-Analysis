function [ ypr ] = aspect_rate( filename )
  y = csvread('good_rate.csv');
  ytr = y(1:10000);
  yte = y(10001:14440);

  x = csvread(filename);
  xtr = x((1:10000),:);
  xte = x((10001:14440),:);
  [beta,l] = VI_beta( xtr,ytr );
  ypr = xte*beta;
end