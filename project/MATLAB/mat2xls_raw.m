%利用matlab在excel中画图
Excel = actxserver('Excel.Application');
set(Excel,'Visible',1);
Workbooks = Excel.Workbooks;
Workbook = Workbooks.invoke('Add');
Sheet1=Workbook.Sheets.Item(1);
RowHeight = 3*ones(1,1000);
ColumnWidth = 3/8*ones(1,1000);

Sheet1.Range('A1:A1000').RowHeight = RowHeight;
Sheet1.Range('A1:ALL1').ColumnWidth = ColumnWidth;
%图片读取
img = imread('243504908.jpg');

%颜色的定义
dou = im2double(img);
[m,n,l] = size(dou);
excel_color = zeros(m,n);
for i=1:n
    for j=1:m
        excel_color(j,i) = 255*dou(j,i,1)+65280*dou(j,i,2)+16711680*dou(j,i,3);
        if i < 703
            if i < 26
                Sheet1.Range([char(64+mod(i,26)),num2str(j)]).Interior.Color = excel_color(j,i);
            elseif i == 26
                Sheet1.Range([char(64+mod(i,26)+26),num2str(j)]).Interior.Color = excel_color(j,i);
            elseif mod(i,26) == 0
                Sheet1.Range([char(64+fix(i/26)-1),char(64+mod(i,26)+26),num2str(j)]).Interior.Color = excel_color(j,i);
            else
                Sheet1.Range([char(64+fix(i/26)),char(64+mod(i,26)),num2str(j)]).Interior.Color = excel_color(j,i);
            end
            
        else
            if mod(i,26) == 0
                Sheet1.Range([char(65),char(64+fix(i/26)-26),char(64+mod(i,26)+26),num2str(j)]).Interior.Color = excel_color(j,i);
            else
                Sheet1.Range([char(65),char(64+fix(i/26)-25),char(64+mod(i,26)),num2str(j)]).Interior.Color = excel_color(j,i);
            end
            
        end
        
            
    end
end
