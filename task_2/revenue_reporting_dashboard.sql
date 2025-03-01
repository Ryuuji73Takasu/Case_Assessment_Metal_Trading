-- revenue_reporting_dashboard.sql
-- Aggregates revenue and profit metrics by buyer_company using both
-- booked and confirmed fields.
-- Adjust the project and dataset references as needed.

SELECT
  buyer_company,
  COUNT(*) AS total_deals,
  -- Booked metrics
  SUM(booked_gross_revenue) AS total_booked_revenue,
  SUM(booked_gross_profit)  AS total_booked_profit,
  ROUND(AVG(booked_gross_profit), 2) AS avg_booked_profit_per_deal,

  -- Confirmed metrics
  SUM(confirmed_gross_revenue) AS total_confirmed_revenue,
  SUM(confirmed_gross_profit)  AS total_confirmed_profit,
  ROUND(AVG(confirmed_gross_profit), 2) AS avg_confirmed_profit_per_deal

FROM `vanilla-steel-case-assessment.vanillasteel_case_assessment.deals`
GROUP BY buyer_company
ORDER BY total_booked_revenue DESC;
