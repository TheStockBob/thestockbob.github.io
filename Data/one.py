import pandas as pd
import requests
import os

from datetime import datetime, timedelta

tickers = ['AAGR', 'ACON', 'ADAG', 'ADIL', 'AFIB', 'AGE', 'AIH', 'AIRJ', 'AKAN', 'AKLI', 'ALBT', 'ALLG', 'AMBO', 'ANGH', 'ANTE', 'APLT', 'APVO', 'ATCH', 'AUNA', 'AUUD', 'AUVI', 'AVGR', 'AVTX', 'BACK', 'BCG', 'BENF', 'BETS', 'BGLC', 'BGXX', 'BIAF', 'BKKT', 'BKYI', 'BMR', 'BNAI', 'BNED', 'BNZI', 'BOF', 'BOLD', 'BQ', 'BRLS', 'BROG', 'BRSH', 'BTR', 'BTSG', 'BTTR', 'BTTX', 'BURU', 'BZFD', 'CACO', 'CADL', 'CAUD', 'CCTG', 'CDTG', 'CERO', 'CETY', 'CHNR', 'CHR', 'CHRO', 'CHSN', 'CING', 'CISO', 'CISS', 'CJET', 'CLDI', 'CLRO', 'CMND', 'CNXA', 'COCH', 'CONX', 'COOT', 'CRML', 'CURO', 'CXAI', 'CYTH', 'CYTO', 'CZOO', 'DBGI', 'DHAI', 'DJT', 'DOGZ', 'DTCK', 'DTSS', 'EBS', 'EDUC', 'EFOI', 'EFSH', 'EGOX', 'EIGR', 'EJH', 'ELAB', 'ELEV', 'ELWS', 'ENSC', 'ENVB', 'EQ', 'ETAO', 'EVAX', 'FAAS', 'FBLG', 'FEAM', 'FFIE', 'FGEN', 'FNCH', 'FOXO', 'FTEL', 'FUFU', 'GBNH', 'GCTS', 'GGE', 'GLMD', 'GMDA', 'GNPX', 'GNS', 'GPAK', 'GRDI', 'GROM', 'GRRR', 'GTI', 'GUTS', 'GVH', 'HAO', 'HCTI', 'HGAS', 'HNRA', 'HOUR', 'HOVR', 'HPCO', 'HRYU', 'HUBC', 'HWH', 'ICCM', 'IDAI', 'IDEX', 'IFBD', 'IMCC', 'IMRN', 'INBS', 'INPX', 'INTJ', 'IONM', 'IVP', 'IVVD', 'JAGX', 'JAN', 'JL', 'JOAN', 'JTAI', 'JYD', 'KA', 'KAVL', 'KDLY', 'KIQ', 'KITT', 'KULR', 'KYTX', 'LASE', 'LEDS', 'LGCL', 'LGVN', 'LIAN', 'LICY', 'LIDR', 'LIFW', 'LITM', 'LIXT', 'LOBO', 'LOT', 'LPA', 'LPTV', 'LQR', 'LRHC', 'LSF', 'LVTX', 'LYT', 'MAMO', 'MCAF', 'MDAI', 'MDIA', 'MGAM', 'MGIH', 'MGOL', 'MGX', 'MIMO', 'MMA', 'MNDR', 'MNPR', 'MNTS', 'MOBX', 'MOTS', 'MRNO', 'MVLA', 'MYSZ', 'NCNA', 'NEPT', 'NEXI', 'NIVF', 'NKGN', 'NKTX', 'NMHI', 'NNOX', 'NRBO', 'NUKK', 'NUWE', 'NVFY', 'NXL', 'ONCO', 'ONMD', 'OPGN', 'OPTT', 'ORGS', 'OTLK', 'OTRK', 'PALI', 'PBLA', 'PBM', 'PCSA', 'PHGE', 'PIK', 'PIXY', 'PMNT', 'PNST', 'POL', 'PRSO', 'PRST', 'PRZO', 'PST', 'PTN', 'PTPI', 'PXMD', 'QLI', 'QNRX', 'QSG', 'QTI', 'RAYA', 'RELI', 'REVB', 'RNAZ', 'RNLX', 'ROI', 'ROMA', 'RVSN', 'RYDE', 'SEED', 'SELX', 'SGLY', 'SGMT', 'SGN', 'SIDU', 'SILO', 'SINT', 'SLNA', 'SMFL', 'SMX', 'SMXT', 'SNAL', 'SNOA', 'SOC', 'SPCB', 'SPRC', 'SST', 'STI', 'SUGP', 'SVMH', 'SWIN', 'SYNX', 'TAOP', 'TBIO', 'TBLT', 'TCBP', 'TCON', 'TCRT', 'TELO', 'TENX', 'TGL', 'THAR', 'TIRX', 'TIVC', 'TNON', 'TPET', 'TPHS', 'TRNR', 'TRUG', 'TURB', 'TVGN', 'TWG', 'UBXG', 'UMAC', 'VANI', 'VCIG', 'VERB', 'VHAI', 'VIEW', 'VIRC', 'VTVT', 'VVPR', 'WAVE', 'WETG', 'WETH', 'WLDS', 'WORX', 'WRNT', 'YIBO', 'YTEN', 'ZBAO', 'ZCMD', 'ZEO', 'ZFOX', 'ZJYL', 'ZOOZ', 'ZPTA', 'ZVSA']

# Define yesterday's date
yesterday = datetime.now() - timedelta(days=2)
yesterday_str = yesterday.strftime('%Y-%m-%d')

# Iterate through tickers and corresponding dates
for ticker in tickers:
    # Update the API call with yesterday's date
    url = f"https://api.marketdata.app/v1/stocks/candles/30/{ticker}?from={yesterday_str}&to={yesterday_str}&extended=true&token=M00xRDd1NUs3bmxOZW9sc2oxWDdQWTRWZXcwNGtxRms2TXI4cEE5UUVPRT0"
    
    # Send request and handle response
    response = requests.get(url)
    data = response.json()
    
    # Check if data is available
    if data.get('s') == 'no_data':
        print(f"No Data for {ticker}")
        continue

    # Convert Unix timestamps to datetime and subtract 5 hours
    data['t'] = pd.to_datetime(data['t'], unit='s') - pd.Timedelta(hours=5)

    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Define file path
    file_path = f'{ticker}.csv'
    
    # Check if file exists
    if os.path.exists(file_path):
        # Read existing data
        existing_data = pd.read_csv(file_path)
        
        # Append new data to existing data
        combined_data = pd.concat([existing_data, df], ignore_index=True)
    else:
        # If file does not exist, use the new data as combined data
        combined_data = df
    
    # Export combined DataFrame to CSV
    combined_data.to_csv(file_path, index=False)

    # Print confirmation message
    print(f"Sheet '{ticker}' saved.")
