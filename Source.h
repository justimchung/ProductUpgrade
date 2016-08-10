#include<vector>

/**
Test whether p can be k-dominated by q or not.
If p is k-dominated by q then return true, else return false.
*/
bool kDomByPoint(std::vector<int> &p, std::vector<int> &q, int k);
bool kDomByPoints(std::vector<int> &p, std::vector<std::vector<int> > &buffer, int k);
std::vector<std::vector<int>> retrieveKDomSkyline(std::vector< std::vector<int> > &buffer, int k);
int getCostCython(std::vector<int> &pUpgrade, std::vector<int> &pOriginal);