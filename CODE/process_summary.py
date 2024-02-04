import pandas as pd
class ProcessSummary:
    def generate_summary_data(self,processed_data,intervals):

        final_data={'fours':[],'sixs':[],'wickets':[]}

        for key,value in processed_data.items():
            for switch in value:
                start=switch-10
                stop=switch+10
                for i in intervals:
                    if switch > i:
                        start=i
                    elif switch <= i:
                        stop=i
                        final_data[key].append((start,stop-2))
                        break
        # print(final_data)
        return final_data


    def process_summary(self,df,merged_df):
        df['runs'] = pd.to_numeric(df['runs'], errors='coerce')
        df['wickets'] = pd.to_numeric(df['wickets'], errors='coerce')
        df['secs'] = pd.to_numeric(df['secs'], errors='coerce')
        run_diff = df['runs'].diff()
        wickets_diff=df['wickets'].diff()
        increase_by_4 = df[run_diff == 4]
        increase_by_6 = df[run_diff == 6]
        increase_by_1=df[wickets_diff==1]
        processed_data={'fours':increase_by_4['secs'].tolist(),
                        'sixs': increase_by_6['secs'].tolist(),
                        'wickets':increase_by_1['secs'].tolist()
                        }
        df=merged_df
        df['checkpoint'] = (df['scorecard'] & df['bowler']).astype(int)
        
        bowler_df = df[df['checkpoint'] == 1]
        # print(bowler_df)

        df = bowler_df.groupby('sec', as_index=False).agg('min')
        df['sec'] = pd.to_numeric(df['sec'], errors='coerce')
       
        # Calculate the difference between consecutive sec values
        diff = df['sec'].diff()

        # Find the indices where the difference is not equal to 1
        indices = diff[diff == 1].index
        print(indices)
        # Merge rows with consecutive sec values where the difference is one
        df = df.drop(indices)
        # Print the merged DataFrame
        # print(df['sec'].values)
        return self.generate_summary_data(processed_data,df['sec'].values)

def main():
    df=pd.read_csv('./CSV/ocr_data.csv')
    merged_df=pd.read_csv('./CSV/merged_df.csv')
    data=ProcessSummary().process_summary(df,merged_df)
    print("final result is ",data)


if __name__ =="__main__":
    main()