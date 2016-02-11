h0 = 2277;   % Height of the top of the mountain (m)
R = 4;      % Radius of the mountain (km)
%endinitvalues

% Grid for x, y values (km)
x = linspace(-10, 10, 41);
y = x;
[xv, yv] = meshgrid(x, y);

hv = h0./(1 + (xv.^2+yv.^2)/(R^2));      % Elevation coordinates (m)
% endinitgrid

s = linspace(0, 2*pi, 100);
curve_x = 10*(1 - s/(2*pi)).*cos(s);
curve_y = 10*(1 - s/(2*pi)).*sin(s);
curve_z = h0./(1 + 100*(1 - s/(2*pi)).^2/(R^2));
% endparamcurve




% Simple plot of mountain

figure(1)
mesh(xv, yv, hv);

% Simple plot of mountain and parametric curve
figure(2)
surf(xv, yv, hv);
colormap winter

% add the parametric curve. LineWidth controls the width of the curve
hold on
plot3(curve_x, curve_y, curve_z, 'LineWidth', 20);
% endsimpleplots




% Define a coarser grid for the vector field
x2 = linspace(-10, 10, 11);
y2 = x2;
[x2v, y2v] = meshgrid(x2, y2);
h2v = h0./(1 + (x2v.^2 + y2v.^2)/(R^2)); % Surface on coarse grid
% endcoarsergrid

% startgradient
[dhdx, dhdy] = gradient(h2v); % dh/dx, dh/dy
% endgradient


% Default two-dimensional contour plot with 7 colored lines
figure(3)
contour(xv, yv, hv);
axis equal

% Default three-dimensional contour plot
figure(4)
contour3(xv, yv, hv);



% View the contours by displaying as an image
figure(6)
pcolor(hv/max(max(abs(hv))));

% 10 contour lines (equally spaced contour levels)
figure(7)
contour(xv, yv, hv, 10);
axis equal

% 10 black ('k') contour lines
figure(8)
contour(xv, yv, hv, 10, 'k');
axis equal

% Specify the contour levels explicitly as a list
figure(9)
levels = [500, 1000, 1500, 2000];
contour(xv, yv, hv, levels);
axis equal

% Add labels with the contour level for each contour line
figure(10)
cs = contour(xv, yv, hv);
clabel(cs, 'FontSize',12);
axis equal
%end contourplots






% Draw contours and gradient field of h
figure(11)
quiver(x2v, y2v, dhdx, dhdy, 'color', [1 0 0]);
hold on
contour(xv, yv, hv);
axis equal
% end draw contours and gradient field of h



% set font

figure(1)
ax = gca;
ax.XAxis.FontSize = 24;
ax.YAxis.FontSize = 24;
ax.ZAxis.FontSize = 24;
print('images/simple_plot_matlab_tocrop','-dpdf')
print('images/simple_plot_matlab','-dpng')

figure(2)
ax = gca;
ax.XAxis.FontSize = 24;
ax.YAxis.FontSize = 24;
ax.ZAxis.FontSize = 24;
print('images/simple_plot_colours_matlab_tocrop','-dpdf')
print('images/simple_plot_colours_matlab','-dpng')

% Save contour plots

figure(3)
ax = gca;
ax.XAxis.FontSize = 24;
ax.YAxis.FontSize = 24;
print('images/default_contour_matlab_tocrop','-dpdf')
print('images/default_contour_matlab','-dpng')

figure(4)
ax = gca;
ax.XAxis.FontSize = 24;
ax.YAxis.FontSize = 24;
ax.ZAxis.FontSize = 24;
print('images/default_contour3_matlab_tocrop','-dpdf')
print('images/default_contour3_matlab','-dpng')

figure(6)
ax = gca;
ax.XAxis.FontSize = 24;
ax.YAxis.FontSize = 24;
print('images/contour_imshow_matlab_tocrop','-dpdf')
print('images/contour_imshow_matlab','-dpng')

figure(7)
ax = gca;
ax.XAxis.FontSize = 24;
ax.YAxis.FontSize = 24;
print('images/contour_10levels_matlab_tocrop','-dpdf')
print('images/contour_10levels_matlab','-dpng')

figure(8)
ax = gca;
ax.XAxis.FontSize = 24;
ax.YAxis.FontSize = 24;
print('images/contour_10levels_black_matlab_tocrop','-dpdf')
print('images/contour_10levels_black_matlab','-dpng')

figure(9)
ax = gca;
ax.XAxis.FontSize = 24;
ax.YAxis.FontSize = 24;
print('images/contour_speclevels_matlab_tocrop','-dpdf')
print('images/contour_speclevels_matlab','-dpng')

figure(10)
ax = gca;
ax.XAxis.FontSize = 24;
ax.YAxis.FontSize = 24;
print('images/contour_clabel_matlab_tocrop','-dpdf')
print('images/contour_clabel_matlab','-dpng')


% Save vector field plots

figure(11)
ax = gca;
ax.XAxis.FontSize = 12;
ax.YAxis.FontSize = 12;
print('images/quiver_matlab_advanced_tocrop','-dpdf')
print('images/quiver_matlab_advanced','-dpng')