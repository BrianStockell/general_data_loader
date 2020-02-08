from company_specific_loaders import *
import argparse

parser = argparse.ArgumentParser('Backlog data file loader and generator')
parser.add_argument('--company', dest='company', action='store', default=None)
args = parser.parse_args()

if __name__ == '__main__':
    companies_list = []
    json_filename = 'general_input.json'

    if json_filename:
        with open(json_filename, 'r') as f:
            datastore = json.load(f)

    for cur_object in datastore['objects']:
        
    # default_columns = datastore['default_config']['default_columns_type']
    # db_config = datastore['default_config']['db_config']
    # root_directory = datastore['default_config']['root_directory']
    # final_collated_table_name = datastore['default_config']['final_collated_table']
    
    # if args.company is not None:

    #     company = next((item for item in datastore['companies'] if item['name'] == args.company), None)
        
    #     class_name = company['class_name']
    #     company_name = company['name']
    #     profile_name = company['profile_name']
    #     company_path = root_directory + company['info']['company_path']
    #     mapped_key_types = company['info']['mapped_key_types']
    #     mapped_company_to_final_col = company['info']['mapped_company_to_final_col']
    #     try:
    #         file_ext = company['info']['file_ext']
    #     except:
    #         file_ext = ''
    #     kwargs_dict ={
    #                     "db_config":db_config,
    #                     "company_path":company_path,
    #                     "mapped_key_types":mapped_key_types,
    #                     "mapped_company_to_final_col":mapped_company_to_final_col,
    #                     "default_columns_type":default_columns,
    #                     "company_name":company_name,
    #                     "final_collated_table_name":final_collated_table_name,
    #                     "profile_name":profile_name,
    #                     "file_ext":file_ext
    #                 }
    #     class_instance = mapped_company_classes[company_name](**kwargs_dict)
    #     print('Running the following company: ', profile_name)
    #     class_instance.main_run_loader()

    # else:
        
    #     for company in datastore['companies']:

    #         class_name = company['class_name']
    #         company_name = company['name']
    #         profile_name = company['profile_name']
    #         company_path = root_directory + company['info']['company_path']
    #         mapped_key_types = company['info']['mapped_key_types']
    #         mapped_company_to_final_col = company['info']['mapped_company_to_final_col']
    #         try:
    #             file_ext = company['info']['file_ext']
    #         except:
    #             file_ext = ''
    #         kwargs_dict ={
    #                         "db_config":db_config,
    #                         "company_path":company_path,
    #                         "mapped_key_types":mapped_key_types,
    #                         "mapped_company_to_final_col":mapped_company_to_final_col,
    #                         "default_columns_type":default_columns,
    #                         "company_name":company_name,
    #                         "final_collated_table_name":final_collated_table_name,
    #                         "profile_name":profile_name,
    #                         "file_ext":file_ext
    #                     }
    #         try:
    #             class_instance = mapped_company_classes[company_name](**kwargs_dict)
    #             print('Running the following company: ', profile_name)
    #             class_instance.main_run_loader()
    #         except:
    #             pass
            