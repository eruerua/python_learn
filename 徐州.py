from pyecharts.charts import Map
from pyecharts import options as opts

districts = ['泉山区', '鼓楼区', '云龙区', '贾汪区', '铜山区', '睢宁县', '邳州市', '新沂市', '沛县', '丰县']
num=[4,3,3,7,0,7,14,2,7,2]
location_price=[list(i) for i in zip(districts,num)]


#%%

map_1=Map()
map_1.set_global_opts(
    title_opts=opts.TitleOpts(title=""),
    visualmap_opts=opts.VisualMapOpts(is_show=True, min_=min(num), max_=max(num))  #最大数据范围
    )
map_1.add("", location_price, maptype="徐州")
map_1.render('map1.html')