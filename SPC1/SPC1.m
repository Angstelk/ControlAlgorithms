pkg load control
%transmitancja ma postac 1/(as^2 + bs + c)
s1=-100+2i
s2=-100-2i
s=tf('s')
%function[void]=plot_resp(s1,s2)
m=poly([s1 s2]);
K=1/(s^2*m(1)+s*m(2)+m(3))
subplot(3,1,1)
step(K)
subplot(3,1,2)
impulse(K)
subplot(3,1,3)
rlocus(K)
grid on;
%`end
plot_resp(s1,s2)
% +-  -- +
