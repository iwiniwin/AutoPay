# -*- coding: utf-8 -*-
# @Author: iwiniwin
# @Date:   2018-02-01 10:33:33
# @Last Modified by:   LensarZhang
# @Last Modified time: 2020-06-01 17:06:32
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import wx
import os
import json


class FileDropTarget(wx.FileDropTarget):  
	def __init__(self, window):  
		wx.FileDropTarget.__init__(self)  
		self.window = window  

	def OnDropFiles(self,  x,  y, fileNames):  
		wx._button.SetLabel("")
		t = ExtractThread(fileNames)
		# ret = t.get_result()
		# if ret == True:
		# 	wx.MessageBox("提取成功",'Info',wx.OK|wx.ICON_INFORMATION)
		# else:
		# 	wx.MessageBox("提取失败 ：" + str(ret), 'Error', wx.YES_DEFAULT | wx.ICON_ERROR)
		return True

class MyFrame(wx.Frame):

    def __init__(self):
		wx.Frame.__init__(self, None, title=u'批量扫码支付',size=(480,320))
		self.Center()
		# self.icon = wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO)
		# self.SetIcon(self.icon)
		panel = wx.Panel(self)
		button = wx.Button(panel, label = u"拖拽区域", size = (480, 290))
		wx._button = button

		self.dropTarget = FileDropTarget(self)  
		self.SetDropTarget(self.dropTarget)

		


if __name__ == "__main__":
	app = wx.App(True)

	frm = MyFrame()
	frm.Show()
	app.MainLoop()
