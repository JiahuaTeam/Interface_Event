# _*_ coding: utf-8 _*_
"""
Time:     2022-03-25 16:13
Author:   Xing Wen Bin
Version:  V 0.1
File:     test_Event_List.py
Describe: 热力地图事件模块，包含事件列表、我的待办等包含其中的各字段查询, Github link: https://github.com/Deeachain/GraphEmbeddings
"""
from xd_api_test.util.config import *
from xd_api_test.util.request_util import RequestUtil
import unittest
class EventList(unittest.TestCase):
    ''' 事件地图：事件列表 '''
    def test_1_All_Event(self):
        ''' 全部事件列表查询 '''
        url ='http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/event/pageEventsPost'
        print(url)
        data ={
          "dealCode": "",
          "sysCode": "",
          "reportType": "",
          "useGridAuth": 'true',
          "userId": "1483681551425028098",
          "pageNum": 1,
          "pageSize": 20,
          "startTime": 1646027760000,
          "endTime": 1648446960000,
          "projectId": "1209302080142258176"
        }
        request = RequestUtil()
        response = request.request(url, 'post', headers=headers, param=data, content_type='application/json')
        print(response)
        self.assertEqual(response['msg'], "新增成功")

    def test_2_Water_Event(self):
        ''' 水环境事件列表查询 '''
        url ='http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/event/pageEventsPost'
        print(url)
        data ={
          "dealCode": "",
          "sysCode": "water",
          "reportType": "",
          "useGridAuth": 'true',
          "userId": "1483681551425028098",
          "pageNum": 1,
          "pageSize": 20,
          "startTime": 1646027760000,
          "endTime": 1648446960000,
          "projectId": "1209302080142258176"
        }
        request = RequestUtil()
        response = request.request(url, 'post', headers=headers, param=data, content_type='application/json')
        print(response)
        self.assertEqual(response['msg'], "新增成功")


    def test_3_air4_Event(self):
        ''' 气环境事件列表查询 '''
        url ='http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/event/pageEventsPost'
        print(url)
        data ={
          "dealCode": "",
          "sysCode": "air4",
          "reportType": "",
          "useGridAuth": 'true',
          "userId": "1483681551425028098",
          "pageNum": 1,
          "pageSize": 20,
          "startTime": 1646027760000,
          "endTime": 1648446960000,
          "projectId": "1209302080142258176"
        }
        request = RequestUtil()
        response = request.request(url, 'post', headers=headers, param=data, content_type='application/json')
        print(response)
        self.assertEqual(response['msg'], "新增成功")


class My_to_do(unittest.TestCase):
    ''' 事件地图：我的待办 '''


    def test_1_To_Do_Event(self):
        ''' 我的待办全部事件查询 '''
        url ='http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/event/pageTasks'
        print(url)
        data ={
        'dealCode':'',
        'sysCode':'',
        'reportType':'',
        'useGridAuth':'false',
        'userId': '1483681551425028098',
        'pageNum': '0',
        'pageSize': '20',
        'startTime': '1646027820000',
        'endTime': '1648533420000',
        'operator': '1483681551425028098',
        'status': '0',
        'projectId': '1209302080142258176',

        }
        request = RequestUtil()
        response = request.request(url, 'get', headers=headers, param=data, content_type='application/json')
        print(response)
        self.assertEqual(response['msg'], "查询成功")

    def test_2_To_Do_autou_Event(self):
        ''' 我的待办全部事件查询:自动上报查询 '''
        url ='http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/event/pageTasks'
        print(url)
        data ={
        'dealCode':'',
        'sysCode':'',
        'reportType':'1',
        'useGridAuth':'false',
        'userId': '1483681551425028098',
        'pageNum': '0',
        'pageSize': '20',
        'startTime': '1646027820000',
        'endTime': '1648533420000',
        'operator': '1483681551425028098',
        'status': '0',
        'projectId': '1209302080142258176',

        }
        request = RequestUtil()
        response = request.request(url, 'get', headers=headers, param=data, content_type='application/json')
        print(response)
        self.assertEqual(response['msg'], "查询成功")

    def test_3_To_Do_People_Event(self):

        ''' 我的待办全部事件查询:人工上报查询  '''
        url ='http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/event/pageTasks'
        print(url)
        data ={
        'dealCode':'',
        'sysCode':'',
        'reportType':'2',
        'useGridAuth':'false',
        'userId': '1483681551425028098',
        'pageNum': '0',
        'pageSize': '20',
        'startTime': '1646027820000',
        'endTime': '1648533420000',
        'operator': '1483681551425028098',
        'status': '0',
        'projectId': '1209302080142258176',

        }
        request = RequestUtil()
        response = request.request(url, 'get', headers=headers, param=data, content_type='application/json')
        print(response)
        self.assertEqual(response['msg'], "查询成功")
    def test_4_To_Do_autou_Event(self):
        ''' 我的待办全部事件查询:状态查询  ，已待派遣为例'''
        url ='http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/event/pageTasks'
        print(url)
        data ={
        'dealCode':'1',
        'sysCode':'',
        'reportType':'2',
        'useGridAuth':'false',
        'userId': '1483681551425028098',
        'pageNum': '0',
        'pageSize': '20',
        'startTime': '1646027820000',
        'endTime': '1648533420000',
        'operator': '1483681551425028098',
        'status': '0',
        'projectId': '1209302080142258176',

        }
        request = RequestUtil()
        response = request.request(url, 'get', headers=headers, param=data, content_type='application/json')
        print(response)
        self.assertEqual(response['msg'], "查询成功")

class Heat_Map(unittest.TestCase):
    ''' 事件地图：热力图'''

    def test_statHeatMap(self):
        url = 'http://srv-newgrid-gateway---integrated.jiahuayun-huanbao-dev.rocktl.com/grid/v1/gridbusiness/sta/statHeatMap/1209302080142258176/air4?'
        data = {
            'startTime': '1638288000000', 'endTime': '1648656000000', 'type':'3'
        }
        request = RequestUtil()
        response = request.request(url, 'get', headers=headers, param=data, content_type='application/json')
        print(response)
        self.assertEqual(response['msg'], "查询成功")
if __name__ == '__main__':
    unittest.main(verbosity=2)