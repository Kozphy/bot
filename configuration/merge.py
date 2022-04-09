from abc import ABC, abstractmethod
from pathlib import Path
# from bot.constants import BOT_DIR, DEFAULT_USERDATA_DIR, CONFIG

class merge:
    
    @abstractmethod
    def merge_user_data(self):
        pass
    @abstractmethod 
    def merge_config(self):
        pass

# class merge_user_data_dir_config(merge):
#     def merge_config():
#         return merge_config() 
#     pass
# class merge_user_data_dir_args(merge):

#     pass

# class per_default(merge):
#     def merge_user_data(self, args):
#             return f"{DEFAULT_USERDATA_DIR}"

#     def merge_config(self,args):
#         return f"{CONFIG}"

# class per_args(merge):
#     def merge_user_data(self, args):
#         if args['user_data_dir'] != DEFAULT_USERDATA_DIR:
#             return f"{BOT_DIR}/{args['user_data_dir']}"

#     def merge_config(self,args):
#         return f"{self.merge_user_data(args)}/{args['config']}"

# class per_config(merge):
#     def merge_user_data(self, args):
#         return f"{BOT_DIR}/{args['user_data_dir']}"

#     def merge_config(self,args):
#         return f"{self.merge_user_data(args)}/{args['config']}"


