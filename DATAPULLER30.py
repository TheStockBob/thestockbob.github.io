import pandas as pd
import requests
import pytz


tickers = ['AAGR', 'ACON', 'ADAG', 'ADIL', 'AFIB', 'AGE', 'AIH', 'AIRJ', 'AKAN', 'AKLI', 'ALBT', 'ALLG', 'AMBO', 'ANGH', 'ANTE', 'APLT', 'APVO', 'ATCH', 'AUNA', 'AUUD', 'AUVI', 'AVGR', 'AVTX', 'BACK', 'BCG', 'BENF', 'BETS', 'BGLC', 'BGXX', 'BIAF', 'BKKT', 'BKYI', 'BMR', 'BNAI', 'BNED', 'BNZI', 'BOF', 'BOLD', 'BQ', 'BRLS', 'BROG', 'BRSH', 'BTR', 'BTSG', 'BTTR', 'BTTX', 'BURU', 'BZFD', 'CACO', 'CADL', 'CAUD', 'CCTG', 'CDTG', 'CERO', 'CETY', 'CHNR', 'CHR', 'CHRO', 'CHSN', 'CING', 'CISO', 'CISS', 'CJET', 'CLDI', 'CLRO', 'CMND', 'CNXA', 'COCH', 'CONX', 'COOT', 'CRML', 'CURO', 'CXAI', 'CYTH', 'CYTO', 'CZOO', 'DBGI', 'DHAI', 'DJT', 'DOGZ', 'DTCK', 'DTSS', 'EBS', 'EDUC', 'EFOI', 'EFSH', 'EGOX', 'EIGR', 'EJH', 'ELAB', 'ELEV', 'ELWS', 'ENSC', 'ENVB', 'EQ', 'ETAO', 'EVAX', 'FAAS', 'FBLG', 'FEAM', 'FFIE', 'FGEN', 'FNCH', 'FOXO', 'FTEL', 'FUFU', 'GBNH', 'GCTS', 'GGE', 'GLMD', 'GMDA', 'GNPX', 'GNS', 'GPAK', 'GRDI', 'GROM', 'GRRR', 'GTI', 'GUTS', 'GVH', 'HAO', 'HCTI', 'HGAS', 'HNRA', 'HOUR', 'HOVR', 'HPCO', 'HRYU', 'HUBC', 'HWH', 'ICCM', 'IDAI', 'IDEX', 'IFBD', 'IMCC', 'IMRN', 'INBS', 'INPX', 'INTJ', 'IONM', 'IVP', 'IVVD', 'JAGX', 'JAN', 'JL', 'JOAN', 'JTAI', 'JYD', 'KA', 'KAVL', 'KDLY', 'KIQ', 'KITT', 'KULR', 'KYTX', 'LASE', 'LEDS', 'LGCL', 'LGVN', 'LIAN', 'LICY', 'LIDR', 'LIFW', 'LITM', 'LIXT', 'LOBO', 'LOT', 'LPA', 'LPTV', 'LQR', 'LRHC', 'LSF', 'LVTX', 'LYT', 'MAMO', 'MCAF', 'MDAI', 'MDIA', 'MGAM', 'MGIH', 'MGOL', 'MGX', 'MIMO', 'MMA', 'MNDR', 'MNPR', 'MNTS', 'MOBX', 'MOTS', 'MRNO', 'MVLA', 'MYSZ', 'NCNA', 'NEPT', 'NEXI', 'NIVF', 'NKGN', 'NKTX', 'NMHI', 'NNOX', 'NRBO', 'NUKK', 'NUWE', 'NVFY', 'NXL', 'ONCO', 'ONMD', 'OPGN', 'OPTT', 'ORGS', 'OTLK', 'OTRK', 'PALI', 'PBLA', 'PBM', 'PCSA', 'PHGE', 'PIK', 'PIXY', 'PMNT', 'PNST', 'POL', 'PRSO', 'PRST', 'PRZO', 'PST', 'PTN', 'PTPI', 'PXMD', 'QLI', 'QNRX', 'QSG', 'QTI', 'RAYA', 'RELI', 'REVB', 'RNAZ', 'RNLX', 'ROI', 'ROMA', 'RVSN', 'SEED', 'SELX', 'SGLY', 'SGMT', 'SGN', 'SIDU', 'SILO', 'SINT', 'SLNA', 'SMFL', 'SMX', 'SMXT', 'SNAL', 'SNOA', 'SOC', 'SPCB', 'SPRC', 'SST', 'STI', 'SUGP', 'SVMH', 'SWIN', 'SYNX', 'TAOP', 'TBIO', 'TBLT', 'TCBP', 'TCON', 'TCRT', 'TELO', 'TENX', 'TGL', 'THAR', 'TIRX', 'TIVC', 'TNON', 'TPET', 'TPHS', 'TRNR', 'TRUG', 'TURB', 'TVGN', 'TWG', 'UBXG', 'UMAC', 'VANI', 'VCIG', 'VERB', 'VHAI', 'VIEW', 'VIRC', 'VTVT', 'VVPR', 'WAVE', 'WETG', 'WETH', 'WLDS', 'WORX', 'WRNT', 'YIBO', 'YTEN', 'ZBAO', 'ZCMD', 'ZEO', 'ZFOX', 'ZJYL', 'ZOOZ', 'ZPTA', 'ZVSA']

# Broken - 'FRES', 'RYDE',
# No Data - 'AILE', 'BTOC', 'CELZ', 'DSY', 'JDZG','JUNE', 'MFI', 'MTEN', 'NCI', 'NNE', 'NUVO', 'OKLO', 'RAY', 'RNLO', 'SGT', 'SHMD', 'SIST', 'SML', 'SNC', 'SNGN', 'SRN', 'TRSG', 'VLFS', 'YYGH', 'ZONE',  

# 



# Iterate through tickers and corresponding dates
for i in range(len(tickers)):
    ticker = tickers[i]
    
    url = f"https://api.marketdata.app/v1/stocks/candles/30/{ticker}?from=2024-01-01&to=2024-06-14&extended=true&token=M00xRDd1NUs3bmxOZW9sc2oxWDdQWTRWZXcwNGtxRms2TXI4cEE5UUVPRT0"
    
    # Send request and handle response
    response = requests.get(url)
    data = response.json()
    
    # Check Data
    if data.get('s') == 'no_data':
        print(f"No Data")
        continue

    # Convert Unix timestamps to datetime
    data['t'] = pd.to_datetime(data['t'], unit='s')

    # Subtract 5 hours from each datetime object
    data['t'] = data['t'] - pd.Timedelta(hours=5)

    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Export DataFrame to CSV
    df.to_csv(f'{ticker}.csv', index=False)

    # Print confirmation message
    print(f"Sheet '{ticker}' saved.")
