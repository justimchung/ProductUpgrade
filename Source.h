#include<vector>

/**
Test whether p can be k-dominated by q or not.
If p is k-dominated by q then return true, else return false.
*/
bool kDomByPoint(std::vector<int> &p, std::vector<int> &q, int k);
bool kDomByPoints(std::vector<int> &p, std::vector<std::vector<int> > &buffer, int k);
std::vector<std::vector<int>> retrieveKDomSkyline(std::vector< std::vector<int> > &buffer, int k);
int getCostCython(std::vector<int> &pUpgrade, std::vector<int> &pOriginal);
std::vector<int> getMinCostProductUsingMultipleDim(int currentDIM, std::vector< std::vector<int> > &Skybuffer, std::vector<int> &subspace, std::vector<int> &minCostProduct, std::vector<int> &origionalProduct);
void upgradeProductMultipleDim(int currentDIM, int basedID, std::vector< std::vector<int> > &Skybuffer, std::vector<int> &subspace, std::vector<int> &upgradeProduct);
/**
* copy the content of fromProduct to toProduct
*/
void copyProduct(std::vector<int> &fromProduct, std::vector<int> &toProduct);
