import pandas as pd

def main():
    """
    Task 3: Match supplier materials to buyer preferences and generate a recommendation table, with a pipeline that:
        -joins the supplier data with buyer preferences.
        -dentifies materials that match buyer preferences based on criteria like grade, finish, and thickness.
        -Outputs a table that lists recommended materials for each buyer.
    """

    # 1. Define file paths
    supplier_file_1 = "task_3/supplier_data1.xlsx"
    supplier_file_2 = "task_3/supplier_data2.xlsx"
    buyer_file      = "task_3/buyer_preferences.xlsx"

    # 2. Read Excel files
    df_sup1 = pd.read_excel(supplier_file_1)
    df_sup2 = pd.read_excel(supplier_file_2)
    df_buy  = pd.read_excel(buyer_file)

    # 3. Combine supplier DataFrames
    df_sup = pd.concat([df_sup1, df_sup2], ignore_index=True)

    # 4. Standardize column names
    df_sup.columns = (df_sup.columns
                      .str.lower()
                      .str.strip()
                      .str.replace(" ", "_"))
    df_buy.columns = (df_buy.columns
                      .str.lower()
                      .str.strip()
                      .str.replace(" ", "_"))

    # 5. Rename columns to unify naming
    rename_map_sup = {
        "thickness_(mm)": "thickness",
        "width_(mm)": "width",
        "weight_(kg)": "weight",
        "gross_weight_(kg)": "gross_weight"
    }
    df_sup.rename(columns=rename_map_sup, inplace=True)

    rename_map_buy = {
        "preferred_thickness_(mm)": "preferred_thickness",
        "preferred_width_(mm)": "preferred_width",
        "max_weight_(kg)": "max_weight"
    }
    df_buy.rename(columns=rename_map_buy, inplace=True)

    # 6. Convert columns to consistent types
    # Supplier
    df_sup["grade"] = df_sup["grade"].astype(str)
    df_sup["finish"] = df_sup["finish"].astype(str)
    df_sup["thickness"] = pd.to_numeric(df_sup.get("thickness"), errors="coerce")
    df_sup["width"] = pd.to_numeric(df_sup.get("width"), errors="coerce")

    # If weight is missing, fallback to gross_weight if it exists
    if "weight" not in df_sup.columns:
        df_sup["weight"] = df_sup.get("gross_weight", pd.NA)
    else:
        # If weight column exists, fill from gross_weight only if weight is missing
        if "gross_weight" in df_sup.columns:
            df_sup["weight"] = df_sup["weight"].fillna(df_sup["gross_weight"])

    # Buyer
    df_buy["preferred_grade"] = df_buy["preferred_grade"].astype(str)
    df_buy["preferred_finish"] = df_buy["preferred_finish"].astype(str)
    df_buy["preferred_thickness"] = pd.to_numeric(df_buy.get("preferred_thickness"), errors="coerce")
    df_buy["preferred_width"] = pd.to_numeric(df_buy.get("preferred_width"), errors="coerce")
    df_buy["max_weight"] = pd.to_numeric(df_buy.get("max_weight"), errors="coerce")
    df_buy["min_quantity"] = pd.to_numeric(df_buy.get("min_quantity"), errors="coerce")

    # 7. Drop rows with missing fields required for matching
    required_cols_sup = ["grade", "finish", "thickness", "width", "weight", "quantity"]
    for col in required_cols_sup:
        if col not in df_sup.columns:
            df_sup[col] = pd.NA  # If truly missing, set to NA
    # Drop rows with NA in these fields
    df_sup.dropna(subset=required_cols_sup, inplace=True)

    # If "quantity" doesn't exist, create it. But let's see if it does:
    if "quantity" not in df_sup.columns:
        df_sup["quantity"] = pd.NA

    # 8. Merge on exact (grade == preferred_grade, finish == preferred_finish,
    # thickness == preferred_thickness, width == preferred_width)
    df_matched = df_buy.merge(
        df_sup,
        left_on=["preferred_grade", "preferred_finish", "preferred_thickness", "preferred_width"],
        right_on=["grade", "finish", "thickness", "width"],
        how="inner"
    )

    print(f"\nRows after merging on (grade, finish, thickness, width): {len(df_matched)}")

    # 9. Filter by weight <= max_weight and quantity >= min_quantity if columns exist
    if "max_weight" in df_matched.columns:
        df_matched.dropna(subset=["weight", "max_weight"], inplace=True)
        df_matched = df_matched[df_matched["weight"] <= df_matched["max_weight"]]

    if "min_quantity" in df_matched.columns:
        df_matched.dropna(subset=["quantity", "min_quantity"], inplace=True)
        df_matched = df_matched[df_matched["quantity"] >= df_matched["min_quantity"]]

    print(f"Rows after weight/quantity filters: {len(df_matched)}")
    
    # 10. Renaming the columns for better readability for non-technical users
    final_rename_map = {
    "buyer_id": "Buyer ID",
    "preferred_grade": "Preferred Grade",
    "preferred_finish": "Preferred Finish",
    "preferred_thickness": "Preferred Thickness (mm)",
    "preferred_width": "Preferred Width (mm)",
    "max_weight": "Max Weight (kg)",
    "min_quantity": "Min Quantity",
    "quality/choice": "Quality/Choice",
    "grade": "Grade",
    "finish": "Finish",
    "thickness": "Thickness (mm)",
    "width": "Width (mm)",
    "description": "Description",
    "gross_weight": "Gross Weight (kg)",
    "rp02": "RP02",
    "rm": "RM",
    "quantity": "Quantity",
    "ag": "AG",
    "ai": "AI",
    "material": "Material",
    "article_id": "Article ID",
    "weight": "Weight (kg)",
    "reserved": "Reserved"
}
    # Only renaming columns that actually exist in df_matched
    rename_map_final = {k: v for k, v in final_rename_map.items() if k in df_matched.columns}

    df_matched.rename(columns=rename_map_final, inplace=True)

    # 11. Save final recommendations
    output_file = "task_3/recommendations.csv"
    df_matched.to_csv(output_file, index=False)
    print(f"\nRecommendation table created in task_3 folder: {output_file}")

if __name__ == "__main__":
    main()
