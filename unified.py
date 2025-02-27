#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:12:19 2025

@author: gayathriyerrapragada
"""

import pandas as pd

#Importing Data
hospital_data = pd.read_csv('/Users/gayathriyerrapragada/Downloads/hpt_extract_20250213.csv')
payer_data = pd.read_csv('//Users/gayathriyerrapragada/Downloads/tic_extract_20250213.csv')

#Data Cleaning

#Hospital Data
hospital_data['hospital_name'] = hospital_data['hospital_name'].str.lower().str.replace(' ', '')
hospital_data = hospital_data.rename(columns={
    'hospital_name': 'hospital_name',
    'hospital_state': 'hospital_state',
    'raw_code': 'billing_code',
    'description': 'service_description',
    'payer_name': 'payer_name',
    'plan_name': 'plan_name',
    'standard_charge_negotiated_dollar': 'negotiated_rate_hospital',
    'standard_charge_gross': 'standard_charge_gross',
    'standard_charge_discounted_cash': 'standard_charge_discounted_cash',
    'standard_charge_min': 'standard_charge_min',
    'standard_charge_max': 'standard_charge_max',
    'standard_charge_methodology': 'standard_charge_methodology',
    'last_updated_on': 'last_updated_on'
})
hospital_data['code_type'] = hospital_data['billing_code'].apply(lambda x: 'MS-DRG' if str(x).isdigit() and len(str(x)) <= 3 else 'CPT')
hospital_data = hospital_data[[
    'hospital_name',
    'hospital_state',
    'billing_code',
    'code_type',
    'service_description',
    'payer_name',
    'plan_name',
    'negotiated_rate_hospital',
    'standard_charge_gross',
    'standard_charge_discounted_cash',
    'standard_charge_min',
    'standard_charge_max',
    'standard_charge_methodology',
    'last_updated_on'
]]

#Payer Data
payer_data['payer'] = payer_data['payer'].str.lower().str.replace(' ', '')
payer_data = payer_data.rename(columns={
    'payer': 'payer_name',
    'code': 'billing_code',
    'code_type': 'code_type',
    'rate': 'negotiated_rate_payer'
})

#Checking if 'billing_code' is the same type in both datasets
hospital_data['billing_code'] = hospital_data['billing_code'].astype(str)
payer_data['billing_code'] = payer_data['billing_code'].astype(str)

payer_data = payer_data[[
    'payer_name',
    'network_name',
    'network_id',
    'network_year_month',
    'network_region',
    'billing_code',
    'code_type',
    'ein',
    'taxonomy_filtered_npi_list',
    'modifier_list',
    'billing_class',
    'place_of_service_list',
    'negotiation_type',
    'arrangement',
    'negotiated_rate_payer',
    'cms_baseline_schedule',
    'cms_baseline_rate'
]]

#Data Merging
combined_data = pd.merge(hospital_data, payer_data, on=['payer_name', 'billing_code', 'code_type'], how='inner', suffixes=('_hospital', '_payer'))

#Calculating Difference

# Convert to numeric
combined_data['negotiated_rate_hospital'] = pd.to_numeric(combined_data['negotiated_rate_hospital'], errors='coerce')
combined_data['negotiated_rate_payer'] = pd.to_numeric(combined_data['negotiated_rate_payer'], errors='coerce')

#Calculate the difference between hospital and payer rates
combined_data['rate_difference'] = combined_data['negotiated_rate_hospital'] - combined_data['negotiated_rate_payer']

#Calculate the percentage difference
combined_data['rate_percentage_difference'] = (combined_data['rate_difference'] / combined_data['negotiated_rate_payer']) * 100

#Summary

print("Summary Statistics of Rate Differences:")
print(combined_data['rate_difference'].describe())

print("\nSummary Statistics of Percentage Rate Differences:")
print(combined_data['rate_percentage_difference'].describe())

#Grouped Analysis
print("\nAverage Rate Difference by Code Type:")
print(combined_data.groupby('code_type')['rate_difference'].mean())

#Output
print(combined_data.head())
combined_data.to_csv('combined_data.csv', index=False)