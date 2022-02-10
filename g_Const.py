import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.dcm':
                    print(full_filename)
                    search_fname_set.append(full_filename)
    except PermissionError:
        print(' Error: Search DIR PermissionError ' )


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


# BoneAge Test Info


# For Call by reference / window 스위치 시에는 함수 인자로 driver값을 넘길 때 reference를 넘겨야 정상동작 했는데
# iframe의 경우는 그냥 함수 인자로 value를 넘겨도 정상동작하는 것으로 테스트 결과가 확인 되었다.
# -after- 이게 그냥 되기도 한다. 자동화 끝내고 테스트 명확하게 한번 더 할 필요가 있다.
# 함수 인자로 넘기면 value고 리스트로 넘기면 reference인지 확인도 안해 봤음
Driver_List = []

# Set Path
Current_PATH = os.getcwd()

DCM_FILE_PATH = "C:\Sample_Webauto"
search_fname_set = []
search(DCM_FILE_PATH)
DCM_FILE_NAME = search_fname_set

LOG_FILE_PATH = DCM_FILE_PATH +"\logs"



# Sign 관련 데이터는 초기 설계 되어 데이터를 함수 내에서 직접 만들어 처리해서 없다.
# 굳이 고칠 필요 없어서 그냥 둔다.
Msg_Type_Excel_Fname= "Msg_Type.xlsx"
Msg_Type_data = []

AD_Message_Excel_Fname= "AD_Message.xlsx"
AD_Message_data = []

Send_Num_Excel_Fname= "Send_Num.xlsx"
Send_Num_data = []

Schedule_Send_Msg_Excel_Fname= "Schedule_Send_Msg.xlsx"
Schedule_Send_Msg_data = []

Attach_File_Excel_Fname= "Attach_File.xlsx"
Attach_File_data = []

Msg_subject_And_content_Excel_Fname= "Msg_subject_And_content.xlsx"
Msg_subject_And_content_data = []

Recv_Num_Excel_Fname= "Recv_Num.xlsx"
Recv_Num_data = []

Sending_Excel_Fname= "Send_Excel.xlsx"
Sending_data = []

Reset_Init_Value_Excel_Fname= "Reset_Init_Value.xlsx"
Reset_Init_Value_data = []








# Test Version check
TEST_log = ' ====== TEST_log ====== '


VUNO_CREDIT = 0
BA_1ST = []
BA_2ND = []
BA_3TH = []
BA_RESULT = ''

SAVE_1ST = []
SAVE_2ND = []
SAVE_3TH = []

#Test Menu Select
Select_Menu = 'Full test'


# class By(object):
#     """
#     Set of supported locator strategies.
#     """
#
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"