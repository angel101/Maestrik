#importer
import pickle as pk
#models
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans

import pandas as pd 
class ClusterHelper(object):
  def __init__(self):
      """Constructor por defecto"""
      super(ClusterHelper, self).__init__()
      self.kmeans = pk.load(open('clusters/process/calculateClusters/kmeans.pk','rb'))
      self.gaus = pk.load(open('clusters/process/calculateClusters/gaus.pk','rb'))
      self.userTables = pk.load(open('clusters/process/calculateClusters/userRfmTable.pk','rb'))
  
  def calculateCluster(self, userData):

    userIdentifier = userData['userIdentifier']

    del userData['userIdentifier']

    userData = pd.DataFrame(userData, index=[0])
    
    cluster = int(self.kmeans.predict(userData)[0])
    gausCluster = None
    # segmentate furter the huge 'common' cluster
    if cluster  == 0:
      gausCluster = int(self.gaus.predict(userData)[0])
    return {'cluster': cluster,'subCluster': gausCluster, 'userIdentifier': userIdentifier, 'userRfmScore': self.getRfmScore(userData,userIdentifier)}

  def getRfmScore(self, userData, userIdentifier):
    userData.rename(columns={'last_buy': 'recency', 
                         'times_buy': 'frequency', 
                         'total_buyed': 'monetary_value'}, inplace=True)
    userData['userIdentifier'] = userIdentifier
    tmpUserTable = self.userTables.append(userData)
    quantiles = tmpUserTable.quantile(q=[0.25,0.5,0.75])
    segmented_rfm = tmpUserTable
    segmented_rfm['r_quartile'] = segmented_rfm['recency'].apply(self.RScore, args=('recency',quantiles,))
    segmented_rfm['f_quartile'] = segmented_rfm['frequency'].apply(self.FMScore, args=('frequency',quantiles,))
    segmented_rfm['m_quartile'] = segmented_rfm['monetary_value'].apply(self.FMScore, args=('monetary_value',quantiles,))
    segmented_rfm['RFMScore'] = segmented_rfm.r_quartile.map(str) + segmented_rfm.f_quartile.map(str)  + segmented_rfm.m_quartile.map(str)
    return segmented_rfm[segmented_rfm['userIdentifier'] == userIdentifier]['RFMScore'].values[0]

  def RScore(self, x, p, d):
    if x <= d[p][0.25]:
      return 1
    elif x <= d[p][0.50]:
      return 2
    elif x <= d[p][0.75]: 
      return 3
    else:
      return 4
      
  def FMScore(self, x, p, d):
    if x <= d[p][0.25]:
      return 4
    elif x <= d[p][0.50]:
      return 3
    elif x <= d[p][0.75]: 
      return 2
    else:
      return 1
