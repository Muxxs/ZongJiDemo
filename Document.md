# 踪迹API说明文档

## 数据库结构

### Config.json 结构
|  Name  | Content | type|
|   ---  |   ---   | --- |
| UserID | 用户数量 | int |
| InfroID| 景点数量 | int |

### User.json 结构
| Name| Content | type|
| --- |  ---   |---|
|  ID |  用户ID |int|
| user|  用户名 |str|
|  pw |  密码   |str|
| like|  喜好   |int[]|

### City.json 结构
| Name | Content | type|
| ---  |   ---   | --- |
|  ID  |  城市ID  | int |
| name |  景点名称 | str |
| tag  |  特征    |int[]|

## 特征&喜好
### 分类方法
- 将各种景点进行标签化
- 同样的标签喜好程度标于用户的like中
  - like和tag的数组size相同，一一相对应
