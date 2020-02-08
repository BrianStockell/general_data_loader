from abc import ABC, abstractmethod
import pyodbc
import pandas as pd
import numpy as np
import datetime
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
import re 
import glob
import warnings
import gc
import csv
import openpyxl
import xlrd

class DataLoaderAbstract(ABC):

    @abstractmethod
    def run_company_pre_process(self):
        pass

    def run_company_post_process(self):
        pass

    def main_run_loader(self):
        self.run_company_pre_process()
        self.load_csv_to_mssql()
        self.run_company_post_process()

    def write_dataframe_csv(self, df,path=None):
        print('path: ',path)
        if path is not None:
            df.to_csv(path, sep='|', encoding='utf-8', header=False, index=False, quoting=csv.QUOTE_NONE, escapechar='\\')
        else:
            print('self.clean_merged_file_path: ',self.clean_merged_file_path)
            df.to_csv(self.clean_merged_file_path, sep='|', encoding='utf-8', header=False, index=False, quoting=csv.QUOTE_NONE, escapechar='\\')


    def set_column_types(self,df,column_type_dict):

        for col in column_type_dict:
            df[col] = df[col].astype(column_type_dict[col])
        return df

    def load_csv_to_mssql(self):
        print('\nInserting CSV to MSSQL\n')
        cur = self.conn_string.cursor()
        headers_type_list =['{0} {1}'.format(key, self.default_columns_type[key]) for key in self.default_columns_type]
        headers_string = ",".join(headers_type_list)

        # try:
        #     create_table_query = """
        #             CREATE TABLE {0} (
        #                 {1}
        #             );""".format(self.final_collated_table_name,headers_string)

        #     cur.execute(create_table_query)
        #     conn_string.commit()
        # except:
        #     pass



        bulk_insert_query = """
            BULK INSERT {0}
            FROM '{1}' WITH (
                FIELDTERMINATOR='|',
                ROWTERMINATOR='\n'
                );
            """.format(self.final_collated_table_name, self.clean_merged_file_path)

        print(bulk_insert_query)

        cur.execute(bulk_insert_query)
        self.conn_string.commit()
        cur.close()
        self.conn_string.close()