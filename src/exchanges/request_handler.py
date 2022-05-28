import asyncio
from loguru import logger
from attrs import define, field, Factory
from typing import Dict,List, Any
import ccxt

@define
class Request_handler:
    httpExceptions: Dict[str, Any] = field()

    @httpExceptions.default
    def _httpExceptions(self):
        httpExceptions= {
            '422': ccxt.ExchangeError,
            '418': ccxt.DDoSProtection,
            '429': ccxt.RateLimitExceeded,
            '404': ccxt.ExchangeNotAvailable,
            '409': ccxt.ExchangeNotAvailable,
            '410': ccxt.ExchangeNotAvailable,
            '500': ccxt.ExchangeNotAvailable,
            '501': ccxt.ExchangeNotAvailable,
            '502': ccxt.ExchangeNotAvailable,
            '520': ccxt.ExchangeNotAvailable,
            '521': ccxt.ExchangeNotAvailable,
            '522': ccxt.ExchangeNotAvailable,
            '525': ccxt.ExchangeNotAvailable,
            '526': ccxt.ExchangeNotAvailable,
            '400': ccxt.ExchangeNotAvailable,
            '403': ccxt.ExchangeNotAvailable,
            '405': ccxt.ExchangeNotAvailable,
            '503': ccxt.ExchangeNotAvailable,
            '530': ccxt.ExchangeNotAvailable,
            '408': ccxt.RequestTimeout,
            '504': ccxt.RequestTimeout,
            '401': ccxt.AuthenticationError,
            '511': ccxt.AuthenticationError,
        }
        return httpExceptions

    @classmethod
    def activate(cls):
        return cls()

    # TODO: Exception error
    def request_api(self, fn, req_args=None, async_bool=False):
        if async_bool:
            res = asyncio.run(self.async_request(fn, req_args))
            data = self.process_http_status_code_Exception(res, fn, req_args, async_bool)
            return data

        res = self.common_request(fn, req_args)
        data = self.process_http_status_code_Exception(res, fn, req_args, async_bool)
        return data


    async def async_request(self, fn, req_args_list):
        # TODO: need to fix rate limit
        # reference article: https://nordicapis.com/everything-you-need-to-know-about-api-rate-limiting/
        # In considering use https://github.com/vutran1710/PyrateLimiter, or other method
        task_obj = []
        for req_args in req_args_list:
            task_obj.append(asyncio.create_task(asyncio.to_thread(fn, **req_args)))

        res = await asyncio.gather(*task_obj,
            return_exceptions=True)

        return res

    def common_request(self, fn, req_args):
        """
        not async request
        """
        if req_args is not None:
            res = fn(**req_args)
            return res

        res = fn()

        return res

    # TODO: implement http request Exception handler
    def process_http_status_code_Exception(self, res, fn, req_regs_list, async_bool=False):
        """
        400 - Bad Request -- Invalid request format.
        401 - Unauthorized -- Invalid API Key
        403 - Forbidden or Too Many Requests -- The request is forbidden or Access limit breached.
        404 - Not Found -- The specified resource could not be found.
        405 - Method Not Allowed -- You tried to access the resource with an invalid method.
        415 - Unsupported Media Type. You need to use: application/json.
        500 - Internal Server Error -- We had a problem with our server. Try again later.
        503 - Service Unavailable -- We're temporarily offline for maintenance. Please try again later.
        """
        ## test http error
        # res = Exception(
        #         {
        #             "code": "429",
        #             "msg": "Too Many Requests",
        #         }
        #     )
        # print(res.args)
        # exit()
        if async_bool == True:
            result = []
            for i in range(len(res)):
                if isinstance(res[i], Exception) == True:
                    print(res[i])
                    print(type(res[i]))
                    print(dir(res[i]))
                    print(res[i].args)
                    code = res[i].args.code
                    # TODO: fix too many request issue
                    if self.httpExceptions[code] == ccxt.RateLimitExceeded:
                        logger.error(f"{res[i]}")
                        raise Exception(res[i])
                        # self.request_api(fn, req_regs_list[i], async_bool=True)
                    if self.httpException[code] != ccxt.RateLimitExceeded:
                        logger.error(f"{res[i]}")
                        raise Exception(res[i])
                result.append(res[i])
            return result
        
        if isinstance(res, Exception) == True:
            code = res.args[0]['code']
            print(code)
            if self.httpExceptions[code] == ccxt.RateLimitExceeded:
                logger.error(f"{res}")
                raise Exception(res)
            elif code in self.httpExceptions and code !='429':
                logger.error(f"{res}")
                raise Exception(res)
        return res
