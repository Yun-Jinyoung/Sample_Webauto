import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import g_Const
import pywinauto
import pyautogui
from openpyxl import load_workbook
import tkinter
import sys


# Wait Click
def Ele_Btn_Click(driver, logger, e_type,element_value, obj_text):
    try:
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((e_type, element_value)))
        if obj_text.find('panel_type'):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((e_type, element_value)))
        driver.find_element(e_type, element_value).click()

    except Exception as inst:
        logger.error("[ Failed ] " + obj_text + str(inst))

def Ele_Just_Wait(driver, logger, e_type,element_value, obj_text):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((e_type, element_value)))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((e_type, element_value)))
        time.sleep(1)
        driver.find_element(e_type, element_value).click()

    except Exception as inst:
        logger.error("[ Failed ] Ele_Just_Wait " + obj_text + str(inst))


# Frame Value clear
def Input_Clear(WebElement):
    while WebElement.get_attribute('value') != '' : WebElement.send_keys(Keys.BACKSPACE)

# Select Radio Button
def Element_Input(driver, logger, e_type ,element_value, Input_value, obj_text):
    try:
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((e_type, element_value)))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((e_type, element_value)))
        Input_Clear(driver.find_element(e_type, element_value))
        driver.find_element(e_type, element_value).send_keys(Input_value)

    except Exception as inst:
        logger.error("[ Failed ] " + obj_text + str(inst))

# Wait Clear Input
def Element_Input(driver, logger, e_type ,element_value, Input_value, obj_text):
    try:
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((e_type, element_value)))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((e_type, element_value)))
        Input_Clear(driver.find_element(e_type, element_value))
        driver.find_element(e_type, element_value).send_keys(Input_value)

    except Exception as inst:
        logger.error("[ Failed ] " + obj_text + str(inst))

def Element_Input2(driver, logger, e_type ,element_value, Input_value, obj_text):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((e_type, element_value)))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((e_type, element_value)))
        Input_Clear(driver.find_element(e_type, element_value))

        for ix in range(0,len(Input_value)):
            driver.find_element(e_type, element_value).send_keys(Input_value[ix])

    except Exception as inst:
        logger.error("[ Failed ] " + obj_text + str(inst))

# window file open
def window_fileopen(logger, Full_Path_Filename):
    try :
        time.sleep(2)  # 웹 컽트롤 밖의 오브젝트라 간단하게 2초 대기하도록 한다.
        app = pywinauto.Application().connect(title_re="열기")
        logger.info(" -Upload file- : " + Full_Path_Filename)
        app["Dialog"]["Edit1"].set_text(Full_Path_Filename)
        app["Dialog"]["Edit1"].type_keys('{ENTER}')

    except Exception as inst:
                logger.error("[ Failed ]  - window_fileopen : " +  str(inst))

def Excel_Load_Dataset(logger, Excel_filename, Dataset, obj_text):
    try:
        # excel load
        load_wb = load_workbook('./excel/' + Excel_filename , data_only=True)
        load_ws = load_wb['Sheet1']

        excel_init_count=0
        for row in load_ws.rows:
            if excel_init_count == 0 :
                excel_init_count = 1
                continue
            row_value = []
            for cell in row:
                if cell.column ==2 : continue
                if str(cell.value) == 'None' : cell.value = ''
                row_value.append(cell.value)
            Dataset.append(row_value)

    except Exception as inst:
                logger.error("[ Failed ]  - (Excel_Load_Dataset) Excel load Fail : " + obj_text + str(inst))

def Popup_text(title_text, btn_text ):
    def select_btn(Menu_text):
        g_Const.Select_Menu = Menu_text
        window.destroy()

    window = tkinter.Tk()
    window.title(title_text)
    window.geometry("440x650+700+50")
    window.resizable(False, False)

    if btn_text == 'Full test' :
        popup_pnl   = tkinter.Button(window, relief="solid", background='SkyBlue1', cursor='hand2', width=40, height=2, text=btn_text, command=lambda:select_btn('Full test'))
        popup_pnl.pack(expand=True)

        popup_pnl_a = tkinter.Button(window, relief="solid", background='khaki1', cursor='hand2', width=40, height=2, text="Open Log Folder", command=lambda: os.startfile(g_Const.DCM_FILE_PATH) )
        popup_pnl_a.pack(expand=True)

        popup_pnl1 = tkinter.Button(window, relief="solid",  background='seashell2', cursor='hand2', width=30, text='발송 유형', command=lambda:select_btn('Msg_Type'))
        popup_pnl1.pack(expand=True)
        popup_pnl2 = tkinter.Button(window, relief="solid",  background='seashell2', cursor='hand2', width=30, text='광고 메시지', command=lambda:select_btn('AD_Message'))
        popup_pnl2.pack(expand=True)
        popup_pnl3 = tkinter.Button(window, relief="solid",  background='seashell2', cursor='hand2', width=30, text='발신 번호', command=lambda:select_btn('Send_Num'))
        popup_pnl3.pack(expand=True)
        popup_pnl4 = tkinter.Button(window, relief="solid",  background='seashell2', cursor='hand2', width=30, text='예약 발송', command=lambda:select_btn('Schedule_Send_Msg'))
        popup_pnl4.pack(expand=True)
        popup_pnl5 = tkinter.Button(window, relief="solid",  background='seashell2', cursor='hand2', width=30, text='첨부 파일', command=lambda:select_btn('Attach_File'))
        popup_pnl5.pack(expand=True)
        popup_pnl6 = tkinter.Button(window, relief="solid",  background='seashell2', cursor='hand2', width=30, text='메시지 제목과 내용', command=lambda:select_btn('Msg_subject_And_content'))
        popup_pnl6.pack(expand=True)
        popup_pnl7 = tkinter.Button(window, relief="solid",  background='seashell2', cursor='hand2', width=30, text='수신자 번호', command=lambda:select_btn('Recv_Num'))
        popup_pnl7.pack(expand=True)
        popup_pnl8 = tkinter.Button(window, relief="solid",  background='seashell2', cursor='hand2', width=30, text='보내기', command=lambda:select_btn('Send'))
        popup_pnl8.pack(expand=True)
        popup_pnl9 = tkinter.Button(window, relief="solid",  background='seashell2', cursor='hand2', width=30, text='재입력 및 초기값', command=lambda:select_btn('Reset_Init_Value'))
        popup_pnl9.pack(expand=True)
        popup_pnl10 = tkinter.Button(window, relief="solid",  background='pale green', cursor='hand2', width=30, text='종료', command=lambda:sys.exit("Quit"))
        popup_pnl10.pack(expand=True)

        window.protocol("WM_DELETE_WINDOW", lambda:sys.exit("Quit"))

        window.mainloop()

    else :
        # popup_pnl   = tkinter.Button(window, relief="solid", background='SkyBlue1', cursor='hand2', width=40, height=2, text=btn_text, command=lambda:window.destroy)
        popup_pnl   = tkinter.Button(window, relief="solid", background='SkyBlue1', cursor='hand2', width=40, height=2, text=btn_text, command=lambda:sys.exit("Quit"))
        popup_pnl.pack(expand=True)
        popup_pnl_a = tkinter.Button(window, relief="solid", background='khaki1', cursor='hand2', width=40, height=2, text="Open Log Folder", command=lambda: os.startfile(g_Const.DCM_FILE_PATH) )
        popup_pnl_a.pack(expand=True)

        window.protocol("WM_DELETE_WINDOW", lambda: sys.exit("종료"))
        window.mainloop()