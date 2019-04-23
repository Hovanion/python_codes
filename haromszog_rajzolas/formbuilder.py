# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class FoAblak
###########################################################################

class FoAblak ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Háromszög", pos = wx.DefaultPosition, size = wx.Size( 953,571 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 953,571 ), wx.Size( 953,571 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel3 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"„a” csúcs" ), wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.coordAX = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -500, 500, 3 )
		fgSizer2.Add( self.coordAX, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.coordAY = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -500, 500, -1 )
		fgSizer2.Add( self.coordAY, 0, wx.ALL, 5 )


		sbSizer2.Add( fgSizer2, 1, wx.EXPAND, 5 )


		bSizer3.Add( sbSizer2, 1, wx.EXPAND, 5 )

		self.m_panel5 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetMaxSize( wx.Size( -1,5 ) )

		bSizer3.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"„b” csúcs" ), wx.VERTICAL )

		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText12 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer21.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.coordBX = wx.SpinCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -500, 500, -1 )
		fgSizer21.Add( self.coordBX, 0, wx.ALL, 5 )

		self.m_staticText111 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		fgSizer21.Add( self.m_staticText111, 0, wx.ALL, 5 )

		self.coordBY = wx.SpinCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -500, 500, 2 )
		fgSizer21.Add( self.coordBY, 0, wx.ALL, 5 )


		sbSizer4.Add( fgSizer21, 1, wx.EXPAND, 5 )


		bSizer3.Add( sbSizer4, 1, wx.EXPAND, 5 )

		self.m_panel51 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel51.SetMaxSize( wx.Size( -1,5 ) )

		bSizer3.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"„c” csúcs" ), wx.VERTICAL )

		fgSizer211 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer211.SetFlexibleDirection( wx.BOTH )
		fgSizer211.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText121 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		fgSizer211.Add( self.m_staticText121, 0, wx.ALL, 5 )

		self.coordCX = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -500, 500, -1 )
		fgSizer211.Add( self.coordCX, 0, wx.ALL, 5 )

		self.m_staticText1111 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1111.Wrap( -1 )

		fgSizer211.Add( self.m_staticText1111, 0, wx.ALL, 5 )

		self.coordCY = wx.SpinCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -500, 500, -1 )
		fgSizer211.Add( self.coordCY, 0, wx.ALL, 5 )


		sbSizer5.Add( fgSizer211, 1, wx.EXPAND, 5 )


		bSizer3.Add( sbSizer5, 1, wx.EXPAND, 5 )

		self.m_panel52 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel52.SetMaxSize( wx.Size( -1,5 ) )

		bSizer3.Add( self.m_panel52, 1, wx.EXPAND |wx.ALL, 5 )

		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"számítás" ), wx.VERTICAL )

		fgSizer2111 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2111.SetFlexibleDirection( wx.BOTH )
		fgSizer2111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1211 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Kerület", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1211.Wrap( -1 )

		fgSizer2111.Add( self.m_staticText1211, 0, wx.ALL, 5 )

		self.kerulet = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2111.Add( self.kerulet, 0, wx.ALL, 5 )

		self.m_staticText11111 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Terület", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11111.Wrap( -1 )

		fgSizer2111.Add( self.m_staticText11111, 0, wx.ALL, 5 )

		self.terulet = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2111.Add( self.terulet, 0, wx.ALL, 5 )


		sbSizer6.Add( fgSizer2111, 1, wx.EXPAND, 5 )


		bSizer3.Add( sbSizer6, 1, wx.EXPAND, 5 )

		self.m_panel521 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel521.SetMaxSize( wx.Size( -1,5 ) )

		bSizer3.Add( self.m_panel521, 1, wx.EXPAND |wx.ALL, 5 )

		self.gomb = wx.Button( self.m_panel3, wx.ID_ANY, u"Bezárás", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.gomb, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel3.SetSizer( bSizer3 )
		self.m_panel3.Layout()
		bSizer3.Fit( self.m_panel3 )
		fgSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 2 )

		self.canvas = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 722,466 ), wx.TAB_TRAVERSAL )
		self.canvas.SetMinSize( wx.Size( 722,466 ) )
		self.canvas.SetMaxSize( wx.Size( 722,466 ) )

		fgSizer1.Add( self.canvas, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel2.SetSizer( fgSizer1 )
		self.m_panel2.Layout()
		fgSizer1.Fit( self.m_panel2 )
		bSizer2.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 10 )


		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.menuClose = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"&Kilépés"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuClose.SetBitmap( wx.Bitmap( u"16x16/row 1/8.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu1.Append( self.menuClose )

		self.m_menubar1.Append( self.m_menu1, u"&Fájl" )

		self.m_menu2 = wx.Menu()
		self.menuNevjegy = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"&Névjegy"+ u"\t" + u"Ctrl+I", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuNevjegy.SetBitmap( wx.Bitmap( u"16x16/row 7/8.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu2.Append( self.menuNevjegy )

		self.m_menubar1.Append( self.m_menu2, u"&Súgó" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class NevjegyAblak
###########################################################################

class NevjegyAblak ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 563,276 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel13 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer5.SetMinSize( wx.Size( 300,-1 ) )
		self.m_panel14 = wx.Panel( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,50 ), wx.TAB_TRAVERSAL )
		self.m_panel14.SetMaxSize( wx.Size( -1,50 ) )

		bSizer5.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"wxPyton példaprogram", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer5.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText10 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"©2008. Copyright Izé", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer5.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self.m_panel13, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		bSizer5.Add( self.m_hyperlink1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel13.SetSizer( bSizer5 )
		self.m_panel13.Layout()
		fgSizer6.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self.m_panel12, wx.ID_ANY, wx.Bitmap( u"small-bigol.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_bitmap1, 0, wx.ALL, 20 )


		self.m_panel12.SetSizer( fgSizer6 )
		self.m_panel12.Layout()
		fgSizer6.Fit( self.m_panel12 )
		bSizer4.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


