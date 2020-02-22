clear all;
close all;


t=1:1:5000;
z=(randn(size(t)))/100;
a = 0.5;
b = 6;
u = ones(size(t));
y = zeros(size(t));

for i = 2:length(t)
    y(i) = a*y(i-1) + b*u(i) + z(i);
end

figure(1);
plot(t,y);
hold on;
grid on;

P = 1000*eye(2,2); %Warunek poczatkowy
theta = [0;0];     %Wektor u, y
tmp = 0;
a_wy = [];
b_wy = [];

%u2 = rand(size(t));    %Generowanie szumu na wejscie
u2=ones(size(t))
z2 = randn((size(t))); %Generowanie szumu zaklocajacego
a_wart = [];
b_wart = [];
blad = [];

for i = 1:length(t)   
   Vec = a*tmp+b*u2(i); 
   Y=1;
   phi = [tmp;u2(i)];  
   P_poprzednie = P;   
  disp(P_poprzednie)     
   P = (P_poprzednie - ((P_poprzednie*(phi*phi') * P_poprzednie) / (1 + (phi'*P_poprzednie*phi))));
   theta = theta + P * phi * (Y - (phi' * theta))
   tmp = Y;
   a_wy = [a_wy, theta(1)];
   b_wy = [b_wy, theta(2)];
end
  disp(theta(1))     
  disp(theta(2))     
#{
figure(2);
plot(t, a_wy);
hold on;
grid on;
xlabel ('Numer iteracji');
ylabel ('estymacja a');

figure(3);
plot(t, b_wy);
hold on;
grid on;
xlabel ('Numer iteracji');
ylabel ('estymacja b');



	}#

