
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import g_Const
import WebControl_Function as WCF


def Open_Test_Page(driver, logger):
    try:
        driver.get('file:///c:/Sample_Webauto/main.html')
        Init_browse_check = 0
    except Exception as inst:
        Init_browse_check = -1
        logger.error("[ Check ] File not exist : " + str(inst))


def Negative_Login_Test(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.EXCEL_FNAME_Sign_In, g_Const.Sign_In_data, 'Sign_In')

    try:
        Excel_Msg_Set = []
        Present_Msg_Set = []

        Excel_Msg_Set.append

        iframe = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, 'Xpath_value')))
        driver.switch_to_frame(iframe)

        for login_info in g_Const.Sign_In_data:

            WCF.Element_Input(driver, logger, By.XPATH, 'Xpath_value', str(login_info[1]), 'E-Mail')
            WCF.Element_Input(driver, logger, By.XPATH, 'Xpath_value', str(login_info[2]), 'Password')

            logger.info(" Input [ID/PW] : " + str(login_info[1]) + "   /   " + str(login_info[2]))

            WCF.Ele_Btn_Click(driver, logger, By.XPATH, 'Xpath_value', 'Sign In Btn')

            time.sleep(2)

            Excel_Msg_Set.append((str(login_info[0]), str(login_info[3])))

            try:
                Msg1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/span[2]').text
            except:
                Msg1 = ''

            print(Msg1)
            Present_Msg_Set.append((str(login_info[0]), str(Msg1)))

        driver.switch_to_default_content()

        Excel_Msg_Set == Present_Msg_Set
        if Excel_Msg_Set == Present_Msg_Set:
            logger.info(" [ PASS ] : Negative Login Test ")
        else:
            logger.error(" [ FAILED ] : Negative Login Test ")
            TestNo = 999
            for ix in range(0, len(Excel_Msg_Set)):
                if Excel_Msg_Set[ix] != Present_Msg_Set[ix]:
                    TestNo = Excel_Msg_Set[ix][0]
                    logger.error(" [ FAILED ] : Negative Login Test - Fail TEST CASE No : [" + str(TestNo) + "]")

        (g_Const.Driver_List[0]).switch_to_default_content()  # (BAC.Driver_List[0]).switch_to_frame(iframe) 에서 돌아 오는 코드

        logger.info('Negative_Login_Test')
    except Exception as inst:
        logger.error("[ FAILED ]  -   : " + str(inst))
#---------------------------------------


def F_Msg_Type(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Msg_Type_Excel_Fname, g_Const.Msg_Type_data, 'Msg_Type')

    for Column_data in g_Const.Msg_Type_data:
        WCF.Ele_Btn_Click(driver, logger, By.ID, str(Column_data[1]), 'value')
        logger.info('F_Msg_Type '+ str(Column_data[1]) + ' Click')
        time.sleep(1)

def F_AD_Message(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.AD_Message_Excel_Fname, g_Const.AD_Message_data, 'AD_Message')

    for Column_data in g_Const.AD_Message_data:
        WCF.Ele_Btn_Click(driver, logger, By.ID, str(Column_data[1]), 'value')
        logger.info('F_AD_Message '+ str(Column_data[1]) + ' Click')
        time.sleep(1)

def F_Send_Num(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Send_Num_Excel_Fname, g_Const.Send_Num_data, 'Send_Num')

    for Column_data in g_Const.Send_Num_data:
        WCF.Element_Input(driver, logger, By.XPATH, 'Xpath_value', str(Column_data[1]), 'E-Mail')
        logger.info('F_Send_Num')

def F_Schedule_Send_Msg(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Schedule_Send_Msg_Excel_Fname, g_Const.Schedule_Send_Msg_data, 'Schedule_Send_Msg')

    for Column_data in g_Const.Schedule_Send_Msg_data:
        WCF.Element_Input(driver, logger, By.XPATH, 'Xpath_value', str(Column_data[1]), 'E-Mail')
        logger.info('F_Schedule_Send_Msg')

def F_Attach_File(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Attach_File_Excel_Fname, g_Const.Attach_File_data, 'Attach_File')

    for Column_data in g_Const.Attach_File_data:
        WCF.Element_Input(driver, logger, By.XPATH, 'Xpath_value', str(Column_data[1]), 'E-Mail')
        logger.info('F_Attach_File')

def F_Msg_subject_And_content(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Msg_subject_And_content_Excel_Fname, g_Const.Msg_subject_And_content_data, 'Msg_subject_And_content')

    for Column_data in g_Const.Msg_subject_And_content_data:
        WCF.Element_Input(driver, logger, By.XPATH, 'Xpath_value', str(Column_data[1]), 'E-Mail')
        logger.info('F_Msg_subject_And_content')

def F_Recv_Num(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Recv_Num_Excel_Fname, g_Const.Recv_Num_data, 'Recv_Num')

    for Column_data in g_Const.Recv_Num_data:
        WCF.Element_Input(driver, logger, By.XPATH, 'Xpath_value', str(Column_data[1]), 'E-Mail')
        logger.info('F_Recv_Num')

def F_Sending(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Sending_Excel_Fname, g_Const.Sending_data, 'Sending')

    for Column_data in g_Const.Sending_data:
        WCF.Element_Input(driver, logger, By.XPATH, 'Xpath_value', str(Column_data[1]), 'E-Mail')
        logger.info('F_Send')

def F_Reset_Init_Value(driver, logger):
    WCF.Excel_Load_Dataset(logger, g_Const.Reset_Init_Value_Excel_Fname, g_Const.Reset_Init_Value_data, 'Reset_Init_Value')

    for Column_data in g_Const.Reset_Init_Value_data:
        WCF.Element_Input(driver, logger, By.XPATH, 'Xpath_value', str(Column_data[1]), 'E-Mail')
        logger.info('F_Reset_Init_Value')

def F_Quit(driver, logger):
        logger.info('F_Quit')






















