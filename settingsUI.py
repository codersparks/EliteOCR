# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsUI.ui'
#
# Created: Tue Jun 16 19:31:17 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.setEnabled(True)
        Settings.resize(517, 449)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Settings)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(Settings)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ui_language = QtGui.QComboBox(self.tab)
        self.ui_language.setObjectName(_fromUtf8("ui_language"))
        self.ui_language.addItem(_fromUtf8(""))
        self.ui_language.addItem(_fromUtf8(""))
        self.ui_language.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.ui_language)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.ocr_language = QtGui.QComboBox(self.tab)
        self.ocr_language.setEnabled(True)
        self.ocr_language.setObjectName(_fromUtf8("ocr_language"))
        self.ocr_language.addItem(_fromUtf8(""))
        self.ocr_language.addItem(_fromUtf8(""))
        self.ocr_language.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.ocr_language)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.translate_results = QtGui.QCheckBox(self.tab)
        self.translate_results.setObjectName(_fromUtf8("translate_results"))
        self.verticalLayout_2.addWidget(self.translate_results)
        self.auto_fill = QtGui.QCheckBox(self.tab)
        self.auto_fill.setObjectName(_fromUtf8("auto_fill"))
        self.verticalLayout_2.addWidget(self.auto_fill)
        self.remove_dupli = QtGui.QCheckBox(self.tab)
        self.remove_dupli.setObjectName(_fromUtf8("remove_dupli"))
        self.verticalLayout_2.addWidget(self.remove_dupli)
        self.pause_at_end = QtGui.QCheckBox(self.tab)
        self.pause_at_end.setChecked(False)
        self.pause_at_end.setObjectName(_fromUtf8("pause_at_end"))
        self.verticalLayout_2.addWidget(self.pause_at_end)
        self.delete_files = QtGui.QCheckBox(self.tab)
        self.delete_files.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.delete_files.setObjectName(_fromUtf8("delete_files"))
        self.verticalLayout_2.addWidget(self.delete_files)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.line_5 = QtGui.QFrame(self.tab)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_4.addWidget(self.line_5)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_18 = QtGui.QLabel(self.tab)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_15.addWidget(self.label_18)
        self.user_name = QtGui.QLineEdit(self.tab)
        self.user_name.setObjectName(_fromUtf8("user_name"))
        self.horizontalLayout_15.addWidget(self.user_name)
        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scr_dir = QtGui.QLineEdit(self.tab_2)
        self.scr_dir.setObjectName(_fromUtf8("scr_dir"))
        self.horizontalLayout.addWidget(self.scr_dir)
        self.browse = QtGui.QPushButton(self.tab_2)
        self.browse.setObjectName(_fromUtf8("browse"))
        self.horizontalLayout.addWidget(self.browse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtGui.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lg_dir = QtGui.QLineEdit(self.tab_2)
        self.lg_dir.setObjectName(_fromUtf8("lg_dir"))
        self.horizontalLayout_3.addWidget(self.lg_dir)
        self.lg_browse = QtGui.QPushButton(self.tab_2)
        self.lg_browse.setObjectName(_fromUtf8("lg_browse"))
        self.horizontalLayout_3.addWidget(self.lg_browse)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_3 = QtGui.QFrame(self.tab_2)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.exp_dir = QtGui.QLineEdit(self.tab_2)
        self.exp_dir.setObjectName(_fromUtf8("exp_dir"))
        self.horizontalLayout_2.addWidget(self.exp_dir)
        self.exp_browse = QtGui.QPushButton(self.tab_2)
        self.exp_browse.setObjectName(_fromUtf8("exp_browse"))
        self.horizontalLayout_2.addWidget(self.exp_browse)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.theme = QtGui.QComboBox(self.tab_4)
        self.theme.setObjectName(_fromUtf8("theme"))
        self.theme.addItem(_fromUtf8(""))
        self.theme.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.theme)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_8 = QtGui.QLabel(self.tab_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)
        self.input_size = QtGui.QSpinBox(self.tab_4)
        self.input_size.setMinimum(5)
        self.input_size.setMaximum(200)
        self.input_size.setProperty("value", 30)
        self.input_size.setObjectName(_fromUtf8("input_size"))
        self.horizontalLayout_6.addWidget(self.input_size)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_9 = QtGui.QLabel(self.tab_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)
        self.snippet_size = QtGui.QSpinBox(self.tab_4)
        self.snippet_size.setMinimum(5)
        self.snippet_size.setMaximum(200)
        self.snippet_size.setProperty("value", 30)
        self.snippet_size.setObjectName(_fromUtf8("snippet_size"))
        self.horizontalLayout_7.addWidget(self.snippet_size)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.line_4 = QtGui.QFrame(self.tab_4)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_7.addWidget(self.line_4)
        self.label_10 = QtGui.QLabel(self.tab_4)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_7.addWidget(self.label_10)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_11 = QtGui.QLabel(self.tab_4)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_8.addWidget(self.label_11)
        self.label_color = QtGui.QLineEdit(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_color.sizePolicy().hasHeightForWidth())
        self.label_color.setSizePolicy(sizePolicy)
        self.label_color.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_color.setObjectName(_fromUtf8("label_color"))
        self.horizontalLayout_8.addWidget(self.label_color)
        self.label_color_button = QtGui.QPushButton(self.tab_4)
        self.label_color_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_color_button.setText(_fromUtf8(""))
        self.label_color_button.setObjectName(_fromUtf8("label_color_button"))
        self.horizontalLayout_8.addWidget(self.label_color_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_12 = QtGui.QLabel(self.tab_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_9.addWidget(self.label_12)
        self.input_color = QtGui.QLineEdit(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_color.sizePolicy().hasHeightForWidth())
        self.input_color.setSizePolicy(sizePolicy)
        self.input_color.setMaximumSize(QtCore.QSize(150, 16777215))
        self.input_color.setObjectName(_fromUtf8("input_color"))
        self.horizontalLayout_9.addWidget(self.input_color)
        self.input_color_button = QtGui.QPushButton(self.tab_4)
        self.input_color_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.input_color_button.setText(_fromUtf8(""))
        self.input_color_button.setObjectName(_fromUtf8("input_color_button"))
        self.horizontalLayout_9.addWidget(self.input_color_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_15 = QtGui.QLabel(self.tab_4)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_12.addWidget(self.label_15)
        self.border_color = QtGui.QLineEdit(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.border_color.sizePolicy().hasHeightForWidth())
        self.border_color.setSizePolicy(sizePolicy)
        self.border_color.setMaximumSize(QtCore.QSize(150, 16777215))
        self.border_color.setObjectName(_fromUtf8("border_color"))
        self.horizontalLayout_12.addWidget(self.border_color)
        self.border_color_button = QtGui.QPushButton(self.tab_4)
        self.border_color_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.border_color_button.setText(_fromUtf8(""))
        self.border_color_button.setObjectName(_fromUtf8("border_color_button"))
        self.horizontalLayout_12.addWidget(self.border_color_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_13 = QtGui.QLabel(self.tab_4)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_10.addWidget(self.label_13)
        self.button_color = QtGui.QLineEdit(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_color.sizePolicy().hasHeightForWidth())
        self.button_color.setSizePolicy(sizePolicy)
        self.button_color.setMaximumSize(QtCore.QSize(150, 16777215))
        self.button_color.setObjectName(_fromUtf8("button_color"))
        self.horizontalLayout_10.addWidget(self.button_color)
        self.button_color_button = QtGui.QPushButton(self.tab_4)
        self.button_color_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.button_color_button.setText(_fromUtf8(""))
        self.button_color_button.setObjectName(_fromUtf8("button_color_button"))
        self.horizontalLayout_10.addWidget(self.button_color_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_14 = QtGui.QLabel(self.tab_4)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_11.addWidget(self.label_14)
        self.button_border_color = QtGui.QLineEdit(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_border_color.sizePolicy().hasHeightForWidth())
        self.button_border_color.setSizePolicy(sizePolicy)
        self.button_border_color.setMaximumSize(QtCore.QSize(150, 16777215))
        self.button_border_color.setObjectName(_fromUtf8("button_border_color"))
        self.horizontalLayout_11.addWidget(self.button_border_color)
        self.button_border_color_button = QtGui.QPushButton(self.tab_4)
        self.button_border_color_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.button_border_color_button.setText(_fromUtf8(""))
        self.button_border_color_button.setObjectName(_fromUtf8("button_border_color_button"))
        self.horizontalLayout_11.addWidget(self.button_border_color_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_16 = QtGui.QLabel(self.tab_4)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_13.addWidget(self.label_16)
        self.background_color = QtGui.QLineEdit(self.tab_4)
        self.background_color.setMaximumSize(QtCore.QSize(150, 16777215))
        self.background_color.setObjectName(_fromUtf8("background_color"))
        self.horizontalLayout_13.addWidget(self.background_color)
        self.background_color_button = QtGui.QPushButton(self.tab_4)
        self.background_color_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.background_color_button.setText(_fromUtf8(""))
        self.background_color_button.setObjectName(_fromUtf8("background_color_button"))
        self.horizontalLayout_13.addWidget(self.background_color_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.label_17 = QtGui.QLabel(self.tab_4)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_7.addWidget(self.label_17)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.b1 = QtGui.QPushButton(self.tab_4)
        self.b1.setText(_fromUtf8(""))
        self.b1.setObjectName(_fromUtf8("b1"))
        self.horizontalLayout_14.addWidget(self.b1)
        self.b2 = QtGui.QPushButton(self.tab_4)
        self.b2.setText(_fromUtf8(""))
        self.b2.setObjectName(_fromUtf8("b2"))
        self.horizontalLayout_14.addWidget(self.b2)
        self.b3 = QtGui.QPushButton(self.tab_4)
        self.b3.setText(_fromUtf8(""))
        self.b3.setObjectName(_fromUtf8("b3"))
        self.horizontalLayout_14.addWidget(self.b3)
        self.b4 = QtGui.QPushButton(self.tab_4)
        self.b4.setText(_fromUtf8(""))
        self.b4.setObjectName(_fromUtf8("b4"))
        self.horizontalLayout_14.addWidget(self.b4)
        self.b5 = QtGui.QPushButton(self.tab_4)
        self.b5.setText(_fromUtf8(""))
        self.b5.setObjectName(_fromUtf8("b5"))
        self.horizontalLayout_14.addWidget(self.b5)
        self.clicked_color = QtGui.QLineEdit(self.tab_4)
        self.clicked_color.setObjectName(_fromUtf8("clicked_color"))
        self.horizontalLayout_14.addWidget(self.clicked_color)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.native_dialog = QtGui.QCheckBox(self.tab_3)
        self.native_dialog.setObjectName(_fromUtf8("native_dialog"))
        self.verticalLayout_6.addWidget(self.native_dialog)
        self.horizontal_exp = QtGui.QCheckBox(self.tab_3)
        self.horizontal_exp.setObjectName(_fromUtf8("horizontal_exp"))
        self.verticalLayout_6.addWidget(self.horizontal_exp)
        self.gray_preview = QtGui.QCheckBox(self.tab_3)
        self.gray_preview.setObjectName(_fromUtf8("gray_preview"))
        self.verticalLayout_6.addWidget(self.gray_preview)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Settings)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "Settings", None))
        self.label_4.setText(_translate("Settings", "Interface Language:", None))
        self.ui_language.setItemText(0, _translate("Settings", "en", None))
        self.ui_language.setItemText(1, _translate("Settings", "de", None))
        self.ui_language.setItemText(2, _translate("Settings", "fr", None))
        self.label_6.setText(_translate("Settings", "(restart required)", None))
        self.label_5.setText(_translate("Settings", "OCR Language:", None))
        self.ocr_language.setItemText(0, _translate("Settings", "eng", None))
        self.ocr_language.setItemText(1, _translate("Settings", "deu", None))
        self.ocr_language.setItemText(2, _translate("Settings", "fra", None))
        self.translate_results.setText(_translate("Settings", "Translate results to english on export", None))
        self.auto_fill.setText(_translate("Settings", "Automatically add results with high confidence to the table", None))
        self.remove_dupli.setText(_translate("Settings", "Remove duplicates in table", None))
        self.pause_at_end.setText(_translate("Settings", "Pause \"OCR All\" at the end of a file (recommended with Delete processed images)", None))
        self.delete_files.setText(_translate("Settings", "Delete processed images", None))
        self.label_18.setText(_translate("Settings", "User name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Settings", "General", None))
        self.label.setText(_translate("Settings", "Screenshot Directory:", None))
        self.browse.setText(_translate("Settings", "Browse", None))
        self.label_3.setText(_translate("Settings", "Log Directory (for system names):", None))
        self.lg_browse.setText(_translate("Settings", "Browse", None))
        self.label_2.setText(_translate("Settings", "Export Directory:", None))
        self.exp_browse.setText(_translate("Settings", "Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Settings", "Paths", None))
        self.label_7.setText(_translate("Settings", "Theme:", None))
        self.theme.setItemText(0, _translate("Settings", "default", None))
        self.theme.setItemText(1, _translate("Settings", "dark", None))
        self.label_8.setText(_translate("Settings", "Text input size", None))
        self.label_9.setText(_translate("Settings", "Image snippet size", None))
        self.label_10.setText(_translate("Settings", "For dark theme:", None))
        self.label_11.setText(_translate("Settings", "Label color:", None))
        self.label_12.setText(_translate("Settings", "Text input color:", None))
        self.label_15.setText(_translate("Settings", "Border color:", None))
        self.label_13.setText(_translate("Settings", "Button text color:", None))
        self.label_14.setText(_translate("Settings", "Button border color:", None))
        self.label_16.setText(_translate("Settings", "Background:", None))
        self.label_17.setText(_translate("Settings", "Color palette of the last calibrated screenshot:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Settings", "Layout", None))
        self.native_dialog.setText(_translate("Settings", "Use native file dialog (might ignore default paths)", None))
        self.horizontal_exp.setText(_translate("Settings", "Horizontal export", None))
        self.gray_preview.setText(_translate("Settings", "Grayscale preview image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Settings", "Misc", None))

import res_rc
