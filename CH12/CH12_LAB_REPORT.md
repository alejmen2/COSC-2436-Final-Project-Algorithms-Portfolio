# Lab Report — Chapter 12: K-Nearest Neighbors

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output — the k comparison, the before/after normalization results, and your recommendation.*

```text

```Features and distance
======================================================================
New fruit features (size, redness): [7, 5]
Distance from new fruit to first training fruit [5, 2]: 3.61
3 nearest neighbors to the new fruit:
  features=[6, 4] label=orange
  features=[7, 3] label=orange
  features=[6, 3] label=orange
Predicted label for new fruit: orange

======================================================================
PART 2a: Failure mode -- the wrong k
======================================================================
k= 1 -> predicted label: dog
k= 3 -> predicted label: cat
k=15 -> predicted label: dog
Explanation:
  At k=1, the single nearest neighbor is the mislabeled 'dog'
  outlier sitting right on top of the test point, so a tiny
  labeling mistake in the data completely controls the answer.
  At k=15, EVERY training point is included, so locality no
  longer matters at all -- the prediction just becomes whichever
  class happens to have more members overall (dog, 8 vs 7),
  even though the test point sits inside the cat cluster.

======================================================================
PART 2b: Failure mode -- unscaled features
======================================================================
Raw features (weight in grams, quality rating 1-5):
  Prediction using raw features: junk
Normalized features (0-1 scale):
  Prediction using normalized features: healthy
Explanation:
  With raw features, the weight-in-grams values (hundreds) are
  so much larger than the 1-5 quality scores that distance is
  decided almost entirely by weight -- the quality feature is
  effectively drowned out because grams and stars are not the
  same units. Once every feature is rescaled to 0-1, both
  features contribute fairly, and the prediction changes.

======================================================================
PART 3: Same neighbors, different question -- regression
======================================================================
Classification and regression from the SAME k_nearest() call:
  classify(neighbors)       -> orange
  predict_rating(neighbors) -> 3.33
Predicted rating for Frank on 'Up': 4.67

======================================================================
Reflection
======================================================================
To recommend restaurants, useful features might be: average
price, cuisine type (encoded as a number), distance from home,
and average star rating. If one of those features were the
same value for every restaurant in the dataset (e.g. every
restaurant is in the same city), that feature would add zero
information -- it could never help distinguish one restaurant
from another, since its distance contribution would always be
the same for every comparison.

## Reflection Questions

1. **Explain k-nearest neighbors to someone who has never programmed.**
   K-nearest neighbors is like the saying, birds of a feather flock together, or you are who you hang around.

2. **Two classmates pick k = 1 and k = 15 on the same data and get different answers. What is each one doing wrong, or right?**
both of them can be counted as right or wrong but one of the looks at a more variety of neighbors and data, meanwhile the other one looks at a smaller group of neighbors or data.

3. **Chapter 12 says Netflix-style recommendations work this way. Describe how someone's viewing history becomes the "features."**
they view everything, from pausing, to skipping, to rewinding of different shows or movies over a large scale, knowing what people like make them recommend similar genres and movies and personalize your page to match you.
