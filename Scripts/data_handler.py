# general imports
import os
import pandas as pd


class data_handler():
    def __init__(self, *args, **kwargs):
        self.path = os.path.dirname(os.path.abspath(__file__)).split("\\")
        self.path = self.path[:-1]
        self.path = '\\'.join(self.path)

        self.read_first_meeting_data_frame()
        self.read_other_diseases_data_frame()
        self.read_follow_up()

        self.R_id = 1009
        self.R_date = 0.1



    def Update_R_id(self, num):
        self.R_id = num

    def Update_R_date(self, num):
        self.R_date = num

    def read_first_meeting_data_frame(self):
        path = os.path.join(self.path, r'data\first_meeting_database.csv')
        self.df_first_meeting = pd.read_csv(path, skip_blank_lines=True, na_filter=True,
                                            encoding='utf-8')

        self.df_first_meeting['date'] = pd.to_datetime(self.df_first_meeting['date'], format='%d/%m/%Y',
                                                       errors='coerce')
        self.df_first_meeting['date'] = self.df_first_meeting['date'].dt.date

        self.df_first_meeting['age'] = pd.to_datetime(self.df_first_meeting['age'], format='%d/%m/%Y',
                                                      errors='coerce')
        self.df_first_meeting['age'] = self.df_first_meeting['age'].dt.date


    def write_first_meeting_data_frame(self, dataframe):
        path = os.path.join(self.path, r'data\first_meeting_database.csv')
        dataframe = dataframe.dropna(how='all')
        dataframe.to_csv(path, index=False)
        self.read_first_meeting_data_frame()

    def read_follow_up(self):
        path = os.path.join(self.path, r'data\FollowUp_meetings_database.csv')
        self.df_followUp = pd.read_csv(path,
                                       skip_blank_lines=True,
                                       na_filter=True,
                                       encoding='utf-8')
        self.df_followUp['Fecha'] = pd.to_datetime(self.df_followUp['Fecha'], format='%d/%m/%Y', errors='coerce')
        self.df_followUp['Fecha'] = self.df_followUp['Fecha'].dt.date

    def write_follow_up(self, dataframe):
        path = os.path.join(self.path, r'data\FollowUp_meetings_database.csv')
        dataframe = dataframe.dropna(how='all')
        dataframe.to_csv(path, index=False)
        self.read_follow_up()

    def read_other_diseases_data_frame(self):
        path = os.path.join(self.path, r'data\Other_diseases.csv')
        self.df_other_diseases = pd.read_csv(path, skip_blank_lines=True, na_filter=True,
                                             encoding='utf-8')

    def write_other_diseases_data_frame(self, dataframe):
        path = os.path.join(self.path, r'data\Other_diseases.csv')
        dataframe = dataframe.dropna(how='all')
        dataframe.to_csv(path, index=False)
        self.read_other_diseases_data_frame()
