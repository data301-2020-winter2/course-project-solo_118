# This is the folder for the data analyst

## Method Chaining and Python Programs

### Step1:Build and test your method chains
---

### Step 2: Wrap your method chain(s) in a function¶
---

### Step 3: Move your function into a new .py file
---

[project_functions py file](scripts/ project_functions.py)


In the task5 , we do the anyalst for the data to explore the relationship about *gender*, *training_hour*, and *company_size*. We use some visualization ways.

```
corr = df.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))

sns.pairplot(df)

df.groupby('gender')['training_hours'].nunique().plot(kind = 'bar')
df.groupby('company_type')['training_hours'].nunique().plot(kind = 'bar')
```

We find some interesting results:

1. the **Male"** use the most training_hours in his job and more **Male"** are looking for job than women.
1. the people in **Pvd Ltd** use the most training_hours in his job and looking for a new job.
1. the *gender* and "company_code" has the positive correlation
1. the *gender* and *training_hour* has the negative correlation
1. the *gender* and *company_code* has the negative correlation

> Finally, we conclude the**male** and **Pvd Ltd** like training and looking for the new job. 