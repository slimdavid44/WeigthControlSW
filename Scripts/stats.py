# general imports
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from datetime import datetime
# pySide2 imports
import PySide2
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QMainWindow
from PySide2 import QtWidgets
# Ui imports
from Generated.stats import Ui_Stats
# classes imports
from data_handler import *


class stats(QMainWindow, Ui_Stats):

    def __init__(self, parent, handler, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = os.path.dirname(os.path.abspath(__file__)).split("\\")
        self.path = self.path[:-1]
        self.path = '\\'.join(self.path)
        self.setupUi(self)
        self.parent = parent
        self.handler = handler
        self.tabWidget.tabBar().setTabTextColor(0, QColor(251, 248, 190))
        self.df_first = self.handler.df_first_meeting.copy()
        self.df_follow = self.handler.df_followUp.copy()

        self.range_of_years_comboBox.addItems(['1', '5', '10'])
        self.Obesity_grade_comboBox.addItems(['All', 'Normal', 'Overweight', 'Obesity |', 'Obesity ||', 'Obesity |||'])
        self.Obesity_grade_comboBox_tab4.addItems(
            ['All', 'Normal', 'Overweight', 'Obesity |', 'Obesity ||', 'Obesity |||'])
        self.Age_groups_comboBox.addItems(['All', 'Teens', '20s', '30s', '40s', '50s', '60s', '70<'])
        self.Age_groups_comboBox_tab4.addItems(['All', 'Teens', '20s', '30s', '40s', '50s', '60s', '70<'])
        self.Procedure_comboBox.addItems(
            ['All', 'BAGUA', 'Balón', 'Manga', 'By-pass', 'Otros', 'Re-Operación', 'Procedimiento Pendiente'])
        self.Procedure_comboBox_tab4.addItems(
            ['All', 'BAGUA', 'Balón', 'Manga', 'By-pass', 'Otros', 'Re-Operación', 'Procedimiento Pendiente'])
        self.Months_after_comboBox.addItems(
            ['All', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13-17',
             '18', '19-23', '24', '24<'])
        self.init_dataFrame()
        self.create_simpel_graphs_tab1()
        self.create_simpel_graphs_tab2()
        self.create_interactive_graphs_tab3()
        self.create_interactive_graphs_tab4()
        self.setWindowTitle('Statistics')
        self.setWindowIcon(PySide2.QtGui.QIcon("icon.png"))
        self.Messages()
        self.connectSignalsSlots()


    def connectSignalsSlots(self):
        self.return_to_main_button.clicked.connect(self.move_main)
        self.return_to_main_button_2.clicked.connect(self.move_main)
        self.return_to_main_button_3.clicked.connect(self.move_main)
        self.return_to_main_button_4.clicked.connect(self.move_main)
        self.save_pic_button1.clicked.connect(self.save_image1)
        self.save_pic_button_2.clicked.connect(self.save_image2)
        self.save_pic_button_3.clicked.connect(self.save_image3)
        self.save_pic_button_4.clicked.connect(self.save_image4)
        self.update_tab2.clicked.connect(self.create_simpel_graphs_tab2)
        self.update_tab3.clicked.connect(self.create_interactive_graphs_tab3)
        self.update_tab4.clicked.connect(self.create_interactive_graphs_tab4)

    def init_dataFrame(self):
        bins_for_age = [0, 20, 30, 40, 50, 60, 70, 120]
        bins_labels_age = ['Teens', '20s', '30s', '40s', '50s', '60s', '70<']
        bins_for_Obesity_grade = [0, 26, 31, 36, 40, 120]
        bins_labels_Obesity_grade = ['Normal', 'Overweight', 'Obesity |', 'Obesity ||', 'Obesity |||']
        for index in self.df_first.index:
            if str(self.df_first.iloc[index].at['date']) == "NaT":
                self.df_first.at[index, 'age'] = -1
            else:
                self.df_first.at[index, 'age'] = self.df_first.at[index, 'date'].year - self.df_first.at[
                    index, 'age'].year - ((self.df_first.at[index, 'date'].month,
                                           self.df_first.at[index, 'date'].day) < (
                                              self.df_first.at[index, 'age'].month, self.df_first.at[index, 'age'].day))

        time_from_procedure = []
        weight_lost = []
        weight_lost_percent = []
        BMI_current = []
        over_weight_lost_percent = []
        month_range1317 = [13, 14, 15, 16, 17]
        month_range1923 = [19, 20, 21, 22, 23]

        self.total_dataframe = pd.merge(self.df_follow[['Cedula', 'Peso']], self.df_first[['Cedula', 'age',
                                                                                           'Origen',
                                                                                           'Procedimiento',
                                                                                           'date', 'peso [kg]',
                                                                                           'height [m]']],
                                        on='Cedula', how='left')
        col_names = ['Cedula', 'Current weight', 'Age', 'Origen', 'Procedimiento', 'Procedure Date', 'Primary weight',
                     'height']
        self.total_dataframe.columns = col_names
        for index in self.total_dataframe.index:

            if str(self.df_follow.iloc[index].at['Fecha']) == "NaT":
                time_from_procedure.append(-1)
            else:
                start_date = self.total_dataframe.at[index, 'Procedure Date']
                end_date = self.df_follow.iloc[index]['Fecha']  # represent a date of follow up meeting
                diff_month = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                if diff_month in month_range1317:
                    diff_month = 13
                elif diff_month in month_range1923:
                    diff_month = 19
                elif diff_month >= 25:
                    diff_month = 25
                time_from_procedure.append(diff_month)
            weight_lost1 = self.total_dataframe.at[index, 'Primary weight'] - self.total_dataframe.at[
                index, 'Current weight']
            weight_lost.append(weight_lost1)
            weight_lost_percent.append(
                (self.total_dataframe.at[index, 'Primary weight'] - self.total_dataframe.at[index, 'Current weight']) /
                self.total_dataframe.at[index, 'Primary weight'])
            BMI_current.append(
                self.getBMI(self.total_dataframe.at[index, 'Current weight'], self.total_dataframe.at[index, 'height']))
            ideal_weight = (25 * (self.total_dataframe.at[index, 'height'] ** 2))
            dif_start_ideal = self.total_dataframe.at[index, 'Primary weight'] - ideal_weight
            over_weight_lost_percent.append(weight_lost1 / dif_start_ideal)
        self.total_dataframe['diff_month'] = time_from_procedure
        self.total_dataframe['weight_lost'] = weight_lost
        self.total_dataframe['weight_lost_percent'] = weight_lost_percent
        self.total_dataframe['BMI_current'] = BMI_current
        self.total_dataframe['over_weight_lost_percent'] = over_weight_lost_percent
        self.total_dataframe['Binned_Ages'] = pd.cut(self.total_dataframe['Age'], bins=bins_for_age,
                                                     labels=bins_labels_age)
        self.total_dataframe['Obesity_grade'] = pd.cut(self.total_dataframe['BMI_current'], bins=bins_for_Obesity_grade,
                                                       labels=bins_labels_Obesity_grade)

        self.df_for_age_origin_procedure_perYear = self.total_dataframe.drop_duplicates(subset=['Cedula'])

    def create_simpel_graphs_tab1(self):
        self.wid_graphs = QtWidgets.QWidget(self.tab)
        self.wid_graphs.setGeometry(0, 90, 1550, 400)
        grid_graphs = QtWidgets.QGridLayout(self.wid_graphs)
        list_for_age = [0, 0, 0, 0, 0, 0, 0]
        list_for_origen = [0] * len(self.total_dataframe['Origen'].unique())
        list_for_procedure = [0, 0, 0, 0, 0, 0, 0]
        distinct_origin = self.total_dataframe['Origen'].unique()
        distinct_Procedimiento = self.total_dataframe['Procedimiento'].unique()

        for index in self.df_for_age_origin_procedure_perYear.index:
            if self.df_for_age_origin_procedure_perYear.at[index, 'Age'] == -1:
                continue
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Age'] < 20:
                list_for_age[0] = list_for_age[0] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Age'] <= 29:
                list_for_age[1] = list_for_age[1] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Age'] <= 39:
                list_for_age[2] = list_for_age[2] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Age'] <= 49:
                list_for_age[3] = list_for_age[3] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Age'] <= 59:
                list_for_age[4] = list_for_age[4] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Age'] <= 69:
                list_for_age[5] = list_for_age[5] + 1
            else:
                list_for_age[6] = list_for_age[6] + 1
            if self.df_for_age_origin_procedure_perYear.at[index, 'Origen'] == distinct_origin.item(0):
                list_for_origen[0] = list_for_origen[0] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Origen'] == distinct_origin.item(1):
                list_for_origen[1] = list_for_origen[1] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Origen'] == distinct_origin.item(2):
                list_for_origen[2] = list_for_origen[2] + 1
            else:
                list_for_origen[3] = list_for_origen[3] + 1

            if self.df_for_age_origin_procedure_perYear.at[index, 'Procedimiento'] == distinct_Procedimiento.item(0):
                list_for_procedure[0] = list_for_procedure[0] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Procedimiento'] == distinct_Procedimiento.item(1):
                list_for_procedure[1] = list_for_procedure[1] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Procedimiento'] == distinct_Procedimiento.item(2):
                list_for_procedure[2] = list_for_procedure[2] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Procedimiento'] == distinct_Procedimiento.item(3):
                list_for_procedure[3] = list_for_procedure[3] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Procedimiento'] == distinct_Procedimiento.item(4):
                list_for_procedure[4] = list_for_procedure[4] + 1
            elif self.df_for_age_origin_procedure_perYear.at[index, 'Procedimiento'] == distinct_Procedimiento.item(5):
                list_for_procedure[5] = list_for_procedure[5] + 1
            else:
                list_for_procedure[6] = list_for_procedure[6] + 1

        labels_for_age = ['<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70<']

        fig_graphs = plt.figure(tight_layout=True)
        ax_age, ax_origen, ax_procedure = fig_graphs.subplots(1, 3)

        reacts_age = ax_age.bar(labels_for_age, list_for_age, edgecolor="white", color='tab:blue')
        ax_age.set_title("Patients By Age")
        ax_age.set_xlabel("Age Group")
        ax_age.set_ylabel("frequency")
        ax_age.tick_params(axis='x', rotation=45)
        self.auto_label_for_int(reacts_age, ax_age)

        reacts_origen = ax_origen.bar(distinct_origin, list_for_origen, edgecolor="white", color='tab:blue')
        ax_origen.set_title("Patients By Origen")
        ax_origen.set_xlabel("Origen")
        ax_origen.set_ylabel("frequency")
        ax_origen.tick_params(axis='x', labelsize=10)
        ax_origen.tick_params(axis='x', rotation=45)
        self.auto_label_for_int(reacts_origen, ax_origen)

        reacts_procedure = ax_procedure.bar(distinct_Procedimiento, list_for_procedure, edgecolor="white",
                                            color='tab:blue')
        ax_procedure.set_title("Patients By Procedure")
        ax_procedure.set_xlabel("Type of Procedure")
        ax_procedure.set_ylabel("frequency")
        ax_procedure.tick_params(axis='x', labelsize=8)
        ax_procedure.tick_params(axis='x', rotation=45)
        self.auto_label_for_int(reacts_procedure, ax_procedure)

        self.plot1 = fig_graphs
        canvas_weight = FigureCanvas(fig_graphs)
        grid_graphs.addWidget(canvas_weight, 0, 0)
        self.wid_graphs.show()

    def create_simpel_graphs_tab2(self):
        num_of_years_in_bin = int(self.range_of_years_comboBox.currentText())

        self.wid_graphs = QtWidgets.QWidget(self.tab_2)
        self.wid_graphs.setGeometry(0, 90, 1375, 400)
        grid_graphs = QtWidgets.QGridLayout(self.wid_graphs)

        self.df_groupby = pd.DataFrame()
        self.df_groupby['year'] = self.df_for_age_origin_procedure_perYear['Procedure Date'].apply(
            lambda date: date.year)
        self.df_groupby = self.df_groupby.groupby(['year']).size()
        self.df_groupby.index = self.df_groupby.index.astype('int64')

        values_for_bin = []
        labels_for_bin = []

        if num_of_years_in_bin == 1:
            for index in self.df_groupby.index:
                labels_for_bin.append(index)
                values_for_bin.append(self.df_groupby._get_value(index))
        elif num_of_years_in_bin == 5:
            values_for_bin, labels_for_bin = self.get_bins_with_values()
        else:
            values_for_bin, labels_for_bin = self.get_bins_with_values()
        # ------------------------------------ end of Patient per Year preparation  -------------------------
        labels_for_diff_month = ['Pre-Qx', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13-17',
                                 '18', '19-23', '24', '24<']

        df_for_overweight_lost = self.total_dataframe.groupby(by='diff_month').mean()
        list_for_overweight_lost = df_for_overweight_lost['over_weight_lost_percent'].tolist()
        for item in range(len(list_for_overweight_lost)):
            list_for_overweight_lost[item] = round(list_for_overweight_lost[item], 2)

        fig_graphs = plt.figure(tight_layout=True)
        ax_overweight_lost, ax_per_year = fig_graphs.subplots(1, 2)
        reacts_overweight_lost = ax_overweight_lost.bar(labels_for_diff_month, list_for_overweight_lost,
                                                        edgecolor="white", color='tab:blue')

        ax_overweight_lost.set_title("Month By Overweight Lost %")
        ax_overweight_lost.set_xlabel("Month From Procedure")
        ax_overweight_lost.set_ylabel("Average Overweight Lost")
        ax_overweight_lost.tick_params(axis='x', rotation=45)
        self.auto_label_for_float(reacts_overweight_lost, ax_overweight_lost)

        reacts_per_year = ax_per_year.bar(labels_for_bin, values_for_bin,
                                          edgecolor="white", color='tab:blue')
        ax_per_year.set_title("Patients Per Year")
        ax_per_year.set_xlabel("Year")
        ax_per_year.set_ylabel("Number Of Patients")
        ax_per_year.get_xaxis().set_ticks(labels_for_bin)
        ax_per_year.tick_params(axis='x', rotation=45)
        self.auto_label_for_int(reacts_per_year, ax_per_year)

        self.plot2 = fig_graphs
        canvas_weight = FigureCanvas(fig_graphs)
        grid_graphs.addWidget(canvas_weight, 0, 0)
        self.wid_graphs.show()

    def create_interactive_graphs_tab3(self):
        self.wid_graphs = QtWidgets.QWidget(self.tab_3)
        self.wid_graphs.setGeometry(30, 150, 1500, 400)
        grid_graphs = QtWidgets.QGridLayout(self.wid_graphs)

        current_month_after_serg = self.Months_after_comboBox.currentText()
        if current_month_after_serg == 'All':
            current_month_after_serg = current_month_after_serg
        elif current_month_after_serg == '13-17':
            current_month_after_serg = 13
        elif current_month_after_serg == '19-23':
            current_month_after_serg = 19
        elif current_month_after_serg == '24<':
            current_month_after_serg = 25
        else:
            current_month_after_serg = int(current_month_after_serg)

        current_Obesity_grade = self.Obesity_grade_comboBox.currentText()
        current_Age_groups = self.Age_groups_comboBox.currentText()
        current_Procedure = self.Procedure_comboBox.currentText()
        values_for_bin = []
        labels_for_bin = []

        self.df_after_fillter = self.get_filtered_df(current_month_after_serg, current_Obesity_grade,
                                                     current_Age_groups, current_Procedure, 3)

        if current_month_after_serg == 'All':
            for index in self.df_after_fillter.index:
                if index == '-1':
                    continue
                labels_for_bin.append(index)
                values_for_bin.append(self.df_after_fillter._get_value(index))
        else:
            labels_for_bin.append(self.df_after_fillter.index[0])
            values_for_bin.append(self.df_after_fillter._get_value(labels_for_bin[0]))

        label = 'Frequency of patient per Month flitered by: Month: ' + str(
            current_month_after_serg) + '  Obesity grade: ' + current_Obesity_grade + '  Age: ' + current_Age_groups + '  Procedure ' + current_Procedure

        fig_graphs = plt.figure(tight_layout=True)
        ax_frequency_by_months = fig_graphs.subplots(1)
        reacts_procedure = ax_frequency_by_months.bar(labels_for_bin, values_for_bin, width=0.6, edgecolor="white",
                                                      color='tab:blue')
        ax_frequency_by_months.set_title(label)
        ax_frequency_by_months.set_xlabel("Month From Procedure")
        ax_frequency_by_months.get_xaxis().set_ticks(labels_for_bin)
        ax_frequency_by_months.set_ylabel("Frequency")
        ax_frequency_by_months.set_xlim(-2, 19)
        ax_frequency_by_months.tick_params(axis='x', rotation=45)
        self.auto_label_for_int(reacts_procedure, ax_frequency_by_months)


        self.plot3 = fig_graphs
        canvas_weight = FigureCanvas(fig_graphs)
        grid_graphs.addWidget(canvas_weight, 0, 0)
        self.wid_graphs.show()

    def create_interactive_graphs_tab4(self):
        self.wid_graphs = QtWidgets.QWidget(self.tab_4)
        self.wid_graphs.setGeometry(30, 150, 1500, 400)
        grid_graphs = QtWidgets.QGridLayout(self.wid_graphs)
        current_Obesity_grade = self.Obesity_grade_comboBox_tab4.currentText()
        current_Age_groups = self.Age_groups_comboBox_tab4.currentText()
        current_Procedure = self.Procedure_comboBox_tab4.currentText()
        values_for_bin = []
        labels_for_bin = []

        self.df_after_fillter = self.get_filtered_df('All', current_Obesity_grade,
                                                     current_Age_groups, current_Procedure, 4)

        for index in self.df_after_fillter.index:
            if index == '-1':
                continue
            labels_for_bin.append(index)
            values_for_bin.append(self.df_after_fillter._get_value(index))

        label = 'OverWeight lost per Month flitered by: Obesity grade: ' + current_Obesity_grade + '  Age: ' + current_Age_groups + '  Procedure ' + current_Procedure

        fig_graphs = plt.figure(tight_layout=True)
        ax_frequency_by_months = fig_graphs.subplots(1)
        reacts_procedure = ax_frequency_by_months.bar(labels_for_bin, values_for_bin, width=0.6, edgecolor="white",
                                                      color='tab:blue')
        ax_frequency_by_months.set_title(label)
        ax_frequency_by_months.set_xlabel("Month From Procedure")
        ax_frequency_by_months.get_xaxis().set_ticks(labels_for_bin)
        ax_frequency_by_months.set_ylabel("OverWeight lost [%]")
        ax_frequency_by_months.set_xlim(-1, 18)
        ax_frequency_by_months.tick_params(axis='x', rotation=45)
        self.auto_label_for_float(reacts_procedure, ax_frequency_by_months)

        self.plot4 = fig_graphs
        canvas_weight = FigureCanvas(fig_graphs)
        grid_graphs.addWidget(canvas_weight, 0, 0)
        self.wid_graphs.show()

    def getBMI(self, weight, height):
        bmi = (weight / (height ** 2))
        formatted_bmi = "{:.2f}".format(bmi)
        return float(formatted_bmi)


    def auto_label_for_int(self, rects, ax):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.01 * height,
                    int(height), backgroundcolor='0.85', fontsize='xx-small',
                    ha='center', va='bottom')



    def auto_label_for_float(self, rects, ax):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.01 * height,
                    float(height), backgroundcolor='0.85', fontsize='xx-small',
                    ha='center', va='bottom')

    def save_image1(self):

        desired_folder = os.path.join(self.path, 'pics\\age origen procedure')
        # os.makedirs(desired_folder) # for creating a routh
        today = datetime.now().date()
        name = str('age_origen_procedure') + "_" + str(today)
        full_path = os.path.join(desired_folder, name)
        try:
            self.plot1.savefig(full_path)
            QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_image_saved)
        except FileNotFoundError:
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_folder_not_exist)

    def save_image2(self):
        desired_folder = os.path.join(self.path, 'pics\\overweight patients per year')
        today = datetime.now().date()
        name = str('overweight patients per year') + "_" + str(today)
        full_path = os.path.join(desired_folder, name)
        try:
            self.plot2.savefig(full_path)
            QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_image_saved)
        except FileNotFoundError:
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_folder_not_exist)

    def save_image3(self):
        desired_folder = os.path.join(self.path, 'pics\\Amount of patient filtered')
        today = datetime.now().date()
        name = str('Amount of patient filtered') + "_" + str(today)
        full_path = os.path.join(desired_folder, name)
        try:
            self.plot3.savefig(full_path)
            QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_image_saved)
        except FileNotFoundError:
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_folder_not_exist)

    def save_image4(self):
        desired_folder = os.path.join(self.path, 'pics\Overweight per month filtered')
        today = datetime.now().date()
        name = str('Overweight per month filtered') + "_" + str(today)
        full_path = os.path.join(desired_folder, name)
        try:
            self.plot4.savefig(full_path)
            QtWidgets.QMessageBox.information(self, self.Message_Success, self.Message_image_saved)
        except FileNotFoundError:
            QtWidgets.QMessageBox.information(self, self.Message_Fail, self.Message_folder_not_exist)

    def move_main(self):
        self.close()
        self.wid_graphs.close()
        self.parent.re_show()

    def get_bins_with_values(self):
        jump = int(self.range_of_years_comboBox.currentText())
        time = datetime.now()
        formmeted_time = int(time.strftime("%Y"))
        start_year = (self.df_groupby.index[0])
        bin_for_years = []

        while start_year <= formmeted_time:
            bin_for_years.append(start_year)
            if start_year == formmeted_time:
                break
            start_year += jump
            if start_year > formmeted_time:
                bin_for_years.append(formmeted_time)

        values_for_bin = [0] * (len(bin_for_years) - 1)
        labels_for_bin = ["a"] * (len(bin_for_years) - 1)
        for i in range(len(bin_for_years) - 1):
            for index in self.df_groupby.index:
                if i == len(bin_for_years) - 2:
                    if bin_for_years[i] <= index <= formmeted_time:
                        values_for_bin[i] = values_for_bin[i] + self.df_groupby.at[index]
                elif bin_for_years[i] <= index < bin_for_years[i + 1]:
                    values_for_bin[i] = values_for_bin[i] + self.df_groupby.at[index]
            if i == len(bin_for_years) - 2:
                labels_for_bin[i] = str(bin_for_years[i]) + "-" + str(bin_for_years[i + 1])
            else:
                labels_for_bin[i] = str(bin_for_years[i]) + "-" + str((bin_for_years[i + 1] - 1))
        return values_for_bin, labels_for_bin

    def get_filtered_df(self, current_month_after_serg, current_Obesity_grade, current_Age_groups, current_Procedure,
                        requested_tab):
        self.df = pd.DataFrame()

        if current_month_after_serg == 'All':
            if current_Age_groups == 'All':
                if current_Obesity_grade == 'All':
                    if current_Procedure == 'All':
                        self.df = self.total_dataframe.copy()
                    else:
                        self.df = self.total_dataframe.query('Procedimiento == @current_Procedure')
                else:
                    self.df = self.total_dataframe.query('Obesity_grade == @current_Obesity_grade')
                    if current_Procedure != 'All':
                        self.df = self.df.query('Procedimiento == @current_Procedure')

            else:
                self.df = self.total_dataframe.query('Binned_Ages == @current_Age_groups')
                if current_Obesity_grade == 'All':
                    if current_Procedure != 'All':
                        self.df = self.df.query('Procedimiento == @current_Procedure')
                else:
                    self.df = self.df.query('Obesity_grade == @current_Obesity_grade')
                    if current_Procedure != 'All':
                        self.df = self.df.query('Procedimiento == @current_Procedure')

        else:
            self.df = self.total_dataframe.query('diff_month == @current_month_after_serg')
            if current_Age_groups == 'All':
                if current_Obesity_grade == 'All':
                    if current_Procedure != 'All':
                        self.df = self.df.query('Procedimiento == @current_Procedure')
                else:
                    self.df = self.df.query('Obesity_grade == @current_Obesity_grade')
                    if current_Procedure != 'All':
                        self.df = self.df.query('Procedimiento == @current_Procedure')
            else:
                self.df = self.df.query('Binned_Ages == @current_Age_groups')
                if current_Obesity_grade == 'All':
                    if current_Procedure != 'All':
                        self.df = self.df.query('Procedimiento == @current_Procedure')

                else:
                    self.df = self.df.query('Obesity_grade == @current_Obesity_grade')
                    if current_Procedure != 'All':
                        self.df = self.df.query('Procedimiento == @current_Procedure')

        if requested_tab == 3:
            self.df_after_fillter = self.df.groupby(by='diff_month').size()
            for index in self.df_after_fillter.index:
                self.df_after_fillter.rename(index={index: str(index)}, inplace=True)
            self.df_after_fillter.rename(index={'13': '13-17'}, inplace=True)
            self.df_after_fillter.rename(index={'19': '19-23'}, inplace=True)
            self.df_after_fillter.rename(index={'25': '24<'}, inplace=True)
            return self.df_after_fillter
        else:
            self.df_after_fillter = self.df.groupby(by='diff_month')['over_weight_lost_percent'].mean()
            for index in self.df_after_fillter.index:
                self.df_after_fillter.rename(index={index: str(index)}, inplace=True)
                self.df_after_fillter = self.df_after_fillter.round(decimals=2)
            self.df_after_fillter.rename(index={'13': '13-17'}, inplace=True)
            self.df_after_fillter.rename(index={'19': '19-23'}, inplace=True)
            self.df_after_fillter.rename(index={'25': '24<'}, inplace=True)
            return self.df_after_fillter

    def Messages(self):
            self.Message_image_saved = 'image has been saved!!'
            self.Message_folder_not_exist = 'Folder does not exist'
            self.Message_Success = 'Success'
            self.Message_Fail = 'Fail'