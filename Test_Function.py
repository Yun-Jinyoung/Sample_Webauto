
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import g_Const
import WebControl_Function as WCF
import pywinauto


def Open_Test_Page(driver, logger):
    try:
        driver.get('file:///c:/Sample_Webauto/main.html')
        Init_browse_check = 0
    except Exception as inst:
        Init_browse_check = -1
        logger.error("[ Check ] File not exist : " + str(inst))

def F_Msg_Type(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Msg_Type_Excel_Fname, g_Const.Msg_Type_data, 'Msg_Type')

    for Column_data in g_Const.Msg_Type_data:
        WCF.Ele_Btn_Click(driver, logger, By.ID, str(Column_data[1]), 'value')
        logger.info('F_Msg_Type '+ str(Column_data[1]) + ' Click')
        time.sleep(1)

    logger.info('F_Msg_Type End')

def F_AD_Message(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.AD_Message_Excel_Fname, g_Const.AD_Message_data, 'AD_Message')

    for Column_data in g_Const.AD_Message_data:
        WCF.Ele_Btn_Click(driver, logger, By.ID, str(Column_data[1]), 'value')
        logger.info('F_AD_Message '+ str(Column_data[1]) + ' Click')
        time.sleep(1)

def F_Send_Num(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Send_Num_Excel_Fname, g_Const.Send_Num_data, 'Send_Num')

    for Column_data in g_Const.Send_Num_data:
        driver.find_element(By.ID, 'sendNo').send_keys(str(Column_data[1]))
        logger.info('F_Send_Num  '+ str(Column_data[1]) + ' Click')
        time.sleep(1)

def F_Schedule_Send_Msg(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Schedule_Send_Msg_Excel_Fname, g_Const.Schedule_Send_Msg_data, 'Schedule_Send_Msg')

    for Column_data in g_Const.Schedule_Send_Msg_data:
        driver.find_element_by_name("requestDate").clear()
        driver.find_element(By.NAME, 'requestDate').send_keys(str(Column_data[1]))
        logger.info('F_Schedule_Send_Msg  '+ str(Column_data[1]) + ' Click')
        time.sleep(1)

def F_Attach_File(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Attach_File_Excel_Fname, g_Const.Attach_File_data, 'Attach_File')

    for Column_data in g_Const.Attach_File_data:
        driver.find_element(By.NAME, 'attachFile').send_keys(str(Column_data[1]))
        logger.info('F_Attach_File  '+ str(Column_data[1]) + ' Click')
        time.sleep(1)

    WCF.Ele_Btn_Click(driver, logger, By.ID, 'attachRemoveBtn', 'value')


def F_Msg_subject_And_content(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Msg_subject_And_content_Excel_Fname, g_Const.Msg_subject_And_content_data, 'Msg_subject_And_content')

    for Column_data in g_Const.Msg_subject_And_content_data:
        driver.find_element_by_name("title").clear()
        driver.find_element(By.NAME, 'title').send_keys(str(Column_data[1]))
        driver.find_element_by_name("body").clear()
        driver.find_element(By.NAME, 'body').send_keys(str(Column_data[2]))
        logger.info('F_Msg_subject_And_content  '+ str(Column_data[1]) + ' Click')
        time.sleep(1)

def F_Recv_Num(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Recv_Num_Excel_Fname, g_Const.Recv_Num_data, 'Recv_Num')

    for Column_data in g_Const.Recv_Num_data:
        driver.find_element_by_name("recipientNo").clear()
        driver.find_element(By.NAME, 'recipientNo').send_keys(str(Column_data[1]))
        logger.info('F_Recv_Num  '+ str(Column_data[1]) + ' Click')
        time.sleep(1)

def F_Sending(driver, logger):
    WCF.Ele_Btn_Click(driver, logger, By.ID, 'sendBtn', 'value')
    logger.info('F_Send Click')
    time.sleep(1)


def F_Reset_Init_Value(driver, logger):
    # WCF.Excel_Load_Dataset(logger, g_Const.Reset_Init_Value_Excel_Fname, g_Const.Reset_Init_Value_data, 'Reset_Init_Value')

    WCF.Ele_Btn_Click(driver, logger, By.ID, 'sendTypeSms', 'value')
    WCF.Ele_Btn_Click(driver, logger, By.ID, 'adN', 'value')
    driver.find_element(By.NAME, 'sendNo').send_keys('-')
    driver.find_element_by_name("requestDate").clear()
    driver.find_element_by_name("attachFile").clear()
    driver.find_element_by_name("title").clear()
    driver.find_element_by_name("body").clear()
    driver.find_element_by_name("recipientNo").clear()

    logger.info('F_Reset_Init_Value Click')
    time.sleep(11)


def F_Quit(driver, logger):
        logger.info('F_Quit')






















