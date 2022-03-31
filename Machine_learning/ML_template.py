def getInfo(df, target=None, a=None, b=None, c=None, i=0):
    """ i=0 - first info about DataFrame(df); 
    i=1 - dabl.detect_types()
    i=2 - .describe(include=all) 
    i=3 - .info() 
    i=4 - get .columns 
    i=5 - dabl.plot(df, target)
    i=6 - get Numerical columns
    i=7 - make .hist() by numercial columns
    i=71 - make .hist() by numercial columns - more beauty
    i=72 - make .scatterplots by numercial columns
    i=8 - get Categorical columns (dtype=object)
    i=81 - get class structure
    i=9 - make all countplots
    i=90 - make countplot with a
    i=91 - make boxplot's a with others
    i=92 - make catbox's with a
    i=93 - counplots separeted by a
    i=10 - make corr.matrix with all features
    i=11 - make autovizualization
    i=12 - analys numerical a for normal 
    i=13 - joinplot with numerical a = ox & b = oy
    i=14 - lmplot with numerical a = ox & b = oy
    i=15 - boxplot with numerical a = oy & b = ox
    i=16 - violinplot with numerical a = oy & b = ox
    i=17 - pivot_table with a,b,c
    i=20 - Pandas Profiling

    """

# Libs
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    %matplotlib inline
    import seaborn as sns
    sns.set()
    from scipy import stats
    from scipy.stats import norm, skew
    import os


# Varianses

    if i == 0:
        cat_f = df.dtypes[df.dtypes == "object"].index.values
        num_f = df.dtypes[df.dtypes != "object"].index.values
        x = len(cat_f)
        y = len(num_f)
        print('There is', x, 'Categorical features (put i=8 to get names);',
              'And there is', y, 'Numerical features (put i=6 to get names);i=7 for num.hist(), i=11 for autoviz features',
              'Shape is:', df.shape)
        return df.shape

    if i == 1:
        return dabl.detect_types(df)

    if i == 2:
        print('or use .describe(include=all) ;)')
        return ds.structdata.describe(df)

    if i == 3:
        print('or use .info() ;)')
        return pp.ProfileReport(df)

    if i == 4:
        x = len(df.columns)
        print('You have', x, ' features:')
        return df.columns

    if i == 5:
        if target == None:
            return 'You need put in target'
        else:
            return dabl.plot(df, target_col=target)

    if i == 6:
        num_candidates = df.dtypes[df.dtypes != "object"].index.values
        if 'Id' == num_candidates[0]:
            num_candidates = np.delete(num_candidates, [0])
        x = len(num_candidates)
        print(x, 'Numerical features:')
        return num_candidates

    if i == 7:
        num_can = df.dtypes[df.dtypes != "object"].index.values
        for col in num_can:
            df.hist(col)
        return 'df_numerical.hist()'

    if i == 71:
        return ds.visualizations.histogram(df)

    if i == 72:
        if target == None:
            return 'You need put in target'
        else:
            if isinstance(a, np.ndarray):
                a = a.tolist()
            if a != None:
                return ds.visualizations.scatterplot(train, num_features=a, target=target)
            else:
                num_feats = df.dtypes[df.dtypes != "object"].index.values
                return ds.visualizations.scatterplot(train, num_features=num_feats, target=target)

    if i == 8:
        cat_candidates = df.dtypes[df.dtypes == "object"].index.values
        x = len(cat_candidates)
        print(x, ' Ctegorical features:')
        return cat_candidates

    if i == 81:
        return ds.structdata.class_count(df)

    if i == 9:
        return ds.visualizations.countplot(df)

    if i == 90:
        if a == None:
            return 'You need put in categorical a'
        else:
            return sns.countplot(df[a])

    if i == 91:
        if a == None:
            return 'You need put in categorical a'
        else:
            return ds.visualizations.boxplot(df, target=a)

    if i == 92:
        if a == None:
            return 'You need put in categorical a'
        else:
            return ds.visualizations.catbox(df, target=a)

    if i == 93:
        if a == None:
            return 'You need put in categorical a'
        else:
            return ds.visualizations.countplot(df, separate_by=a)

    if i == 10:
        plt.figure(figsize=(30, 8))
        sns.heatmap(df.corr(), cmap='coolwarm', annot=True)
        return plt.show()

    if i == 11:

        if target == None:
            return 'You need put in target'
        else:
            filename = ""
            sep = ","
            target = target
            dft = AV.AutoViz(
                filename,
                sep,
                target,
                df,
                header=0,
                verbose=0,
                lowess=False,
                chart_format="svg",
                max_rows_analyzed=150000,
                max_cols_analyzed=30,
            )

    if i == 12:
        cat_candidates = df.dtypes[df.dtypes == "object"].index.values
        if a == None:
            return 'You need put in numerical ^a^'
        elif a in cat_candidates:
            return 'a must be nemerical'
        else:
            plt.figure(figsize=(10, 3))
            sns.distplot(df[a], fit=norm)

            (mu, sigma) = norm.fit(df[a])
            print('\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu, sigma))
            plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(
                mu, sigma)], loc='best')
            plt.ylabel('Frequency')
            plt.title(a)
            fig = plt.figure()
            res = stats.probplot(df[a], plot=plt)
            return plt.show()

    if i == 13:
        cat_candidates = df.dtypes[df.dtypes == "object"].index.values
        num_candidates = df.dtypes[df.dtypes != "object"].index.values
        if a == None:
            return 'You need put in numerical a'
        elif a in cat_candidates:
            return 'a must be nemerical'
        elif b == None:
            return 'You need put in nemerical b'
        elif b in cat_candidates:
            return 'b must be nemerical'
        else:
            return sns.jointplot(x=b, y=a, data=df, kind='scatter')
        return 'ok'

    if i == 14:
        cat_candidates = df.dtypes[df.dtypes == "object"].index.values
        num_candidates = df.dtypes[df.dtypes != "object"].index.values
        if a == None:
            return 'You need put in numerical a'
        elif a in cat_candidates:
            return 'a must be nemerical'
        elif b == None:
            return 'You need put in nemerical b'
        elif b in cat_candidates:
            return 'b must be nemerical'
        else:
            return sns.lmplot(x=b, y=a, data=df)

    if i == 15:
        cat_candidates = df.dtypes[df.dtypes == "object"].index.values
        num_candidates = df.dtypes[df.dtypes != "object"].index.values
        if a == None:
            return 'You need put in numerical a'
        elif a in cat_candidates:
            return 'a must be nemerical'
        elif b == None:
            return 'You need put in feature b'
        else:
            plt.figure(figsize=(16, 8))
            sns.boxplot(x=b, y=a, data=df)
            return plt.show()

    if i == 16:
        cat_candidates = df.dtypes[df.dtypes == "object"].index.values
        num_candidates = df.dtypes[df.dtypes != "object"].index.values
        if a == None:
            return 'You need put in numerical a'
        elif a in cat_candidates:
            return 'a must be nemerical'
        elif b == None:
            return 'You need put in categorical b'
        else:
            return sns.violinplot(x=b, y=a, data=df)

    if i == 17:
        cat_candidates = df.dtypes[df.dtypes == "object"].index.values
        num_candidates = df.dtypes[df.dtypes != "object"].index.values
        if a == None:
            return 'You need put in numerical a'
        elif a in cat_candidates:
            return 'a cannot be categorical'
        elif b == None:
            return 'You need put in categorical b'
        elif b in num_candidates:
            return 'b must be categorical'
        elif c == None:
            return 'You need put in categorical c'
        elif c in num_candidates:
            return 'c must be categorical'
        else:
            return df.pivot_table(a, b, c).plot(kind='bar', stacked=True)

    if i == 18:
        cat_candidates = df.dtypes[df.dtypes == "object"].index.values
        num_candidates = df.dtypes[df.dtypes != "object"].index.values
        if a == None:
            return 'You need put in numerical a'
        elif a in cat_candidates:
            return 'a cannot be categorical'
        elif b == None:
            return 'You need put in categorical b'
        elif b in num_candidates:
            return 'b must be categorical'
        elif c == None:
            return 'You need put in categorical c'
        elif c in num_candidates:
            return 'c must be categorical'
        else:
            plt.figure(figsize=(15, 10))
            platform_genre_sales = train.pivot_table(
                index=b,
                columns=c,
                values=a,
                aggfunc=sum).fillna(0).applymap(float)
            return sns.heatmap(platform_genre_sales, annot=True, fmt=".1f", linewidths=.5)

    if i == 20:
        return pp.ProfileReport(df)