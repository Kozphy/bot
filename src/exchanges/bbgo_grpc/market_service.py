from bbgo import MarketService
# import bbgo_pb2
# import bbgo_pb2_grpc
from exchanges.utils.misc import convert_symbols_to_request_format, isodate_to_unixtime
import pprint
import time
import asyncio

class bbgo_market_service():
    def __init__(self, configured, host, port):
        self.config = configured
        # pprint.pprint(self.config)
        # exit()
        self.symbols = convert_symbols_to_request_format(self.config['symbols'])
        self.service = MarketService(host, port)

    # TODO: achieve async effect
    async def grpc_get_kline(self, limit=30, *args, **kwargs):
        c = self.config
        # stub: bbgo_pb2_grpc.MarketServicesStub
        # exit()
        # print(f'limit: {limit}')
        # print(f'args: {args}')
        # print(f'kwargs: {kwargs}')
        start = time.process_time()

        result = []
        for symbol in self.symbols:
            for timeframe in c['timeframes']:
                # print('\n')
                req_para = {
                    'exchange': c['session'],
                    'symbol': symbol,
                    'interval': timeframe,
                    'start_time': isodate_to_unixtime(c['startAt']),
                    'end_time': isodate_to_unixtime(c['endAt']),
                    'limit': limit
                }

                pprint.pprint(req_para)
                print('\n')
                # currently, can't achieve async effect
                klines = await asyncio.gather(asyncio.to_thread(self.service.query_klines, **req_para))
                print(klines)
                # result.append(klines)
        
        end = time.process_time()
        # print(result)
        print(f'process time {end - start}')

        return result


