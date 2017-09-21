#Whattomine.com API for a few coins
whattomine_lookup=dict();
whattomine_lookup['zec']={'name':'zec','url':'https://www.whattomine.com/coins/166.json','algorithm':'eqhash'}
whattomine_lookup['eth']={'name':'eth','url':'https://www.whattomine.com/coins/151.json','algorithm':'ethash'}
whattomine_lookup['dcr']={'name':'dcr','url':'https://www.whattomine.com/coins/152.json','algorithm':'decred'}
whattomine_lookup['sc']={'name':'sc','url':'https://www.whattomine.com/coins/161.json','algorithm':'sia'}
whattomine_lookup['xzc']={'name':'xzc','url':'https://www.whattomine.com/coins/175.json','algorithm':'lyra2z'}
whattomine_lookup['etc']={'name':'etc','url':'https://www.whattomine.com/coins/162.json','algorithm':'ethash'}
whattomine_lookup['grs']={'name':'grs','url':'https://www.whattomine.com/coins/48.json','algorithm':'groestl'};
whattomine_lookup['zcl']={'name':'zcl','url':'https://www.whattomine.com/coins/167.json','algorithm':'eqhash'};
whattomine_lookup['kmd']={'name':'kmd','url':'https://www.whattomine.com/coins/174.json','algorithm':'eqhash'};
whattomine_lookup['pasc']={'name':'pasc','url':'https://www.whattomine.com/coins/172.json','algorithm':'pascal'};

#What algos a coin use.
algo_lookup=dict();
algo_lookup['aur']=['skein','myr-gr'];
algo_lookup['log']='skein2';
algo_lookup['spr']='spread';
algo_lookup['xvg']=['x17','lyra2v2','myr-gr'];
algo_lookup['chc']='c11';
algo_lookup['xlr']='nist5';
algo_lookup['vlt']='veltor';
algo_lookup['sigt']='skunk';
algo_lookup['boat']='hmq1725';
algo_lookup['mona']='lyra2v2';
algo_lookup['vtc']='lyra2v2';
algo_lookup['lbc']='lbry';
algo_lookup['btx']='bitcore';
algo_lookup['j']=['bastion','myr-gr','whirl','luffa','keccak','nist5'];
algo_lookup['dgb']=['skein','myr-gr'];
algo_lookup['orb']='neoscrypt';
algo_lookup['ftc']='neoscrypt';
algo_lookup['bsd']='xevan';
algo_lookup['xre']='x11evo';
algo_lookup['bntly']='x17';



#These coins have multiple algos, getinfo()['pow_algo'] is used to check algo.
multi_algo_coins=['aur','dgb','myr','j'];


#keys to tell what wallet a port corresponds to
wallets_key=dict();
wallets_key['aur']='auroracoin';
wallets_key['log']='woodcoin';
wallets_key['spr']='spreadcoin';
wallets_key['chc']='chaincoin';
wallets_key['xlr']='solariscoin';
wallets_key['vlt']='Veltor';
wallets_key['sigt']='signatum';
wallets_key['boat']='doubloon';
wallets_key['mona']='monacoin';
wallets_key['vtc']='vertcoin';
wallets_key['lbc']='lbrycrd';
wallets_key['btx']='bitcore';
wallets_key['j']='joincoin';
wallets_key['dgb']='digibyte';
wallets_key['ftc']='feathercoin';
wallets_key['bsd']='bitsend';
wallets_key['xre']='revolvercoin';
wallets_key['orb']='orbitcoin';
wallets_key['bntly']='bentleycoin';

#Exchange
exchange=dict();
exchange['zec']=['poloniex','BTC_ZEC']
exchange['etc']=['poloniex','BTC_ETC']
exchange['eth']=['poloniex','BTC_ETH']
exchange['dcr']=['poloniex','BTC_DCR']
exchange['sc']=['poloniex','BTC_SC']
exchange['pasc']=['poloniex','BTC_PASC']
exchange['aur']=['bittrex','BTC-AUR']
exchange['dgb']=['bittrex','BTC-DGB']
exchange['spr']=['bittrex','BTC-SPR']
exchange['xzc']=['bittrex','BTC-XZC']
exchange['ftc']=['bittrex','BTC-FTC']
exchange['lbc']=['bittrex','BTC-LBC']
exchange['vtc']=['bittrex','BTC-VTC']
exchange['xvg']=['bittrex','BTC-XVG']
exchange['mona']=['bittrex','BTC-MONA']
exchange['myr']=['bittrex','BTC-MYR']
exchange['zcl']=['bittrex','BTC-ZCL']
exchange['kmd']=['bittrex','BTC-KMD']
exchange['dmd']=['bittrex','BTC-DMD']
exchange['grs']=['bittrex','BTC-GRS']
exchange['bsd']=['bittrex','BTC-BSD']
exchange['xlr']=['cryptopia','XLR/BTC']
exchange['chc']=['cryptopia','CHC/BTC']
exchange['orb']=['cryptopia','ORB/BTC']
exchange['btx']=['cryptopia','BTX/BTC']
exchange['xre']=['cryptopia','XRE/BTC']
exchange['log']=['ccex','log-btc']
exchange['vlt']=['yobit','vlt_btc']
exchange['boat']=['nova','BTC_BOAT']
exchange['sigt']=['nova','BTC_SIGT']
exchange['j']=['nova','BTC_J']
exchange['bntly']=['','']; #no exchange available

def alias(orig,see,replace,name='',cond=''):
	if orig==see and name==cond:
		return replace;
	else:
		return orig;

def aliases(algo):
	algo=alias(algo,'myr-gr','groestl');
	algo=alias(algo,'groestle','groestl');
	algo=alias(algo,'myriad-groestl','groestl');
	algo=alias(algo,'penta','pentablake');
	algo=alias(algo,'whirl','whirlpool');
	algo=alias(algo,'whirlpoolx','whirlpool');
	algo=alias(algo,'lyra2re','lyra2v2');
	algo=alias(algo,'lyra2rev2','lyra2v2');
	return algo;