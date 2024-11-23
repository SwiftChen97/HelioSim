% 定义线性算子A：二阶导数算子，域为 [-1, 1]，初始值为 0
A = chebop(@(x,u) diff(u,2), [-1, 1], 0);

% 定义电荷分布函数 f，这里使用高斯函数
f = chebfun('exp(-1000*(x+0.3)^6)');

% 清空当前图窗，并绘制电荷分布函数 f，颜色为红色
clf, plot(f, 'r'), hold on;

% 设置初始颜色为红色，并逐步变暗
c = [0.8 0 0]; 

% 设置y轴显示范围，并打开网格
ylim([-.1 1.1]), grid on

% 设置时间步长，逐步演化
for t = [0.01 0.1 0.5]
    % 使用指数算子（exp）求解方程 u(t)，其中 A 是算子，t 是时间步长，f 是初始条件
    u = expm(A, t, f);
    
    % 绘制解 u(t)，颜色根据 c 逐渐变暗
    plot(u,'color', c), c = 0.5*c;  % 每次绘制后，颜色变为原来的50%
end

% 关闭图形保持，使后续的图像不与当前图像重叠
hold off