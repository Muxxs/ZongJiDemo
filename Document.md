# 踪迹开发文档

## 数据库结构

### Config.json 结构
|  Name  | Content | type|
|   ---  |   ---   | --- |
| UserID | 用户数量 | int |
| InfroID| 景点数量 | int |
| PassID | 文章数量 | int |
### User.json 结构
| Name| Content | type|
| --- |  ---   |---|
|  ID |  用户ID |  int|
| user|  用户名 |  str|
|  pw |  密码   |  str|
| like|  喜好   |  int[]|

### City.json 结构
| Name | Content | type|
| ---  |   ---   | --- |
|  ID  |  城市ID  | int |
| name |  景点名称 | str |
| tag  |  特征    |int[]|

### passage.json 结构
| Name | Content | type|
| ---  |   ---   | --- |
| PassageID|  文章ID  | int  |
| AuthorID |  作者ID  | int  |
| Time     |  发布时间 | str  |
| PlaceID  |  涉及景点 | int[]|
| Passage  |  文章内容 | str  |

## 特征&喜好
### 分类方法
- 将各种景点进行标签化
- 同样的标签喜好程度标于用户的like中
  - like和tag的数组size相同，一一相对应
  - `例`
  
    | Name | 1 | 2 | 3 | 4 | 5 | 6 |
    | ---  | --- | --- | --- | --- | --- | --- |
    |  tag 针对景点  |  是否有山  | 是否有水 | 是否有建筑 | 是否中国风 | 是否西式建筑 | 是否有美食 |
    |  like 针对用户 |  是否喜欢山  | 是否喜欢水 | 是否喜欢建筑 | 是否喜欢中国风 | 是否喜欢西式建筑 | 是否喜欢美食 |

    - 具体分类方案后续会联系旅游管理的相关同学进一步确定