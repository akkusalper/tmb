import sqlite3
import argparse

def calculate_TMB(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # Extract non-synonymous coding variants
    cursor.execute("""SELECT COUNT(*) FROM variant WHERE base__coding = 'Y' AND base__so NOT IN ('SYN', 'INT')""")
    non_synonymous_variants = cursor.fetchone()[0]

    # Total number of base pairs examined
    total_base_pairs_examined = 9713257

    # Calculate TMB
    TMB = (non_synonymous_variants / total_base_pairs_examined) * 1_000_000

    # Print the results
    print(f"Number of non-synonymous coding variants: {non_synonymous_variants}")
    print(f"TMB: {TMB:.3f} mutations/Mb")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate TMB from an SQLite database.")
    parser.add_argument("database", help="SQLite database file to process.")
    args = parser.parse_args()
    
    calculate_TMB(args.database)
