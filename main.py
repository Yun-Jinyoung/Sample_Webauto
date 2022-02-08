from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging
import sys
import time
from win32api import GetSystemMetrics

#----- import sub lib call func
import g_Const as g_Const
import Test_Function as TF
import WebControl_Function as WCF
#-------------------------------

if __name__ == '__main__':
    WCF.Popup_text("Automation Test - Ready to start ", "Full test")

    #----- Init Folder
    g_Const.createFolder(g_Const.LOG_FILE_PATH)
    #-----------------------------------------

    #----- Init logger
    logger = logging.getLogger("[ Bone Age ]")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s|[%(lineno)d]|:%(message)s')

    File_time = time.strftime('%Y_%m%d_%H_%M', time.localtime(time.time()))

    ErrorHandler = logging.FileHandler(g_Const.LOG_FILE_PATH+'\\'+File_time+"_Test_Result.log", encoding='utf-8')
    ErrorHandler.setLevel(logging.DEBUG)
    ErrorHandler.setFormatter(formatter)
    logger.addHandler(ErrorHandler)
    #----------------

    logger.info("  ")
    logger.info(g_Const.BA_AUTO_TEST)
    logger.info(" ========== -----  TEST START  ----- ========== ")

    #----- Chrome Browser Init
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    g_Const.Driver_List.append(driver)
    g_Const.ResolutionX = GetSystemMetrics(0)
    g_Const.ResolutionY = GetSystemMetrics(1)
    #---------------------------------------

    TF.Open_Test_Page(driver, logger)

    if g_Const.Select_Menu == 'Full test':
        TF.F_Msg_Type(driver, logger)
        TF.F_AD_Message(driver, logger)
        TF.F_Send_Num(driver, logger)
        TF.F_Schedule_Send_Msg(driver, logger)
        TF.F_Attach_File(driver, logger)
        TF.F_Msg_subject_And_content(driver, logger)
        TF.F_Recv_Num(driver, logger)
        TF.F_Send(driver, logger)
        TF.F_Reset_Init_Value(driver, logger)
        TF.F_Quit(driver, logger)
    else:
        if g_Const.Select_Menu == 'Msg_Type':
            TF.F_Msg_Type(driver, logger)
        if g_Const.Select_Menu == 'AD_Message':
            TF.F_AD_Message(driver, logger)
        if g_Const.Select_Menu == 'Send_Num':
            TF.F_Send_Num(driver, logger)
        if g_Const.Select_Menu == 'Schedule_Send_Msg':
            TF.F_Schedule_Send_Msg(driver, logger)
        if g_Const.Select_Menu == 'Attach_File':
            TF.F_Attach_File(driver, logger)
        if g_Const.Select_Menu == 'Msg_subject_And_content':
            TF.F_Msg_subject_And_content(driver, logger)
        if g_Const.Select_Menu == 'Recv_Num':
            TF.F_Recv_Num(driver, logger)
        if g_Const.Select_Menu == 'Send':
            TF.F_Send(driver, logger)
        if g_Const.Select_Menu == 'Reset_Init_Value':
            TF.F_Reset_Init_Value(driver, logger)
        if g_Const.Select_Menu == 'Quit':
            TF.F_Quit(driver, logger)

    logger.info(" ========== -----  TEST END  ----- ========== ")
    WCF.Popup_text("Automation Test - The end", "Test End")
    sys.exit("종료")