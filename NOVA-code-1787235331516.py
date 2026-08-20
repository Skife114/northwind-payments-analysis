import pandas as pd
import json

def run_analysis():
    # Load raw data
    orders = pd.read_csv('data/orders.csv')
    export = pd.read_csv('data/merchant_dashboard_export.csv')
    fx = pd.read_csv('data/fx_rates.csv')
    
    # Clean text columns
    string_cols = ['merchant_id', 'route_id', 'processor', 'order_type', 'status', 'currency', 'payment_method']
    for col in string_cols:
        orders[col] = orders[col].astype(str).str.strip().str.upper().replace({'NAN': None, 'NONE': None})
        
    orders['created_at'] = pd.to_datetime(orders['created_at'])
    
    # Filter for NOVA-FX SALE attempts
    nova = orders[(orders['merchant_id'] == 'NOVA-FX') & (orders['order_type'] == 'SALE')].copy()
    
    # Adjust for UTC+8 merchant timezone
    nova['created_at_utc8'] = nova['created_at'] + pd.Timedelta(hours=8)
    nova['date_utc8'] = nova['created_at_utc8'].dt.strftime('%Y-%m-%d')
    
    # Filter complete dates (Apr 1 - Jun 28)
    nova_valid = nova[nova['date_utc8'] < '2026-06-29'].copy()
    
    # Metric Summary
    pre_june = nova_valid[nova_valid['date_utc8'] < '2026-06-01']
    post_june = nova_valid[nova_valid['date_utc8'] >= '2026-06-01']
    
    print(f"Pre-June Portal Rate: {sum(pre_june['status']=='APPROVED') / sum(pre_june['status'].isin(['APPROVED', 'DECLINED'])):.2%}")
    print(f"Post-June Portal Rate: {sum(post_june['status']=='APPROVED') / sum(post_june['status'].isin(['APPROVED', 'DECLINED'])):.2%}")

if __name__ == "__main__":
    run_analysis()