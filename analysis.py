import pandas as pd
import json

def run_analysis():
    # Load raw datasets from the data/ directory
    orders = pd.read_csv('data/orders.csv')
    
    # Standardize string fields
    str_cols = ['merchant_id', 'route_id', 'processor', 'order_type', 'status', 'currency', 'payment_method']
    for col in str_cols:
        orders[col] = orders[col].astype(str).str.strip().str.upper().replace({'NAN': None, 'NONE': None})
        
    orders['created_at_dt'] = pd.to_datetime(orders['created_at'])
    
    # Adjust to UTC+8 merchant timezone
    orders['created_at_utc8'] = orders['created_at_dt'] + pd.Timedelta(hours=8)
    orders['date_utc8'] = orders['created_at_utc8'].dt.strftime('%Y-%m-%d')
    
    # Filter for NOVA-FX SALE attempts up to complete days (June 28)
    nova = orders[(orders['merchant_id'] == 'NOVA-FX') & 
                  (orders['order_type'] == 'SALE') & 
                  (orders['date_utc8'] < '2026-06-29')].copy()
    
    pre_june = nova[nova['date_utc8'] < '2026-06-01']
    post_june = nova[nova['date_utc8'] >= '2026-06-01']
    
    # Calculate Portal View Approval Rates
    pre_portal_app = (pre_june['status'] == 'APPROVED').sum()
    pre_portal_att = pre_june['status'].isin(['APPROVED', 'DECLINED']).sum()
    
    post_portal_app = (post_june['status'] == 'APPROVED').sum()
    post_portal_att = post_june['status'].isin(['APPROVED', 'DECLINED']).sum()
    
    print("=== NOVA MARKETS ANALYSIS RESULTS ===")
    print(f"Pre-June Portal Rate:  {pre_portal_app / pre_portal_att:.2%}")
    print(f"Post-June Portal Rate: {post_portal_app / post_portal_att:.2%}")

if __name__ == "__main__":
    run_analysis()