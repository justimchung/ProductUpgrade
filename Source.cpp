#include "Source.h"

bool kDomByPoint(std::vector<int> &p, std::vector<int> &q, int k)
{
	unsigned len = p.size();
	int numWorstDim = 0;
	int NumQualifyDim = 0;
	bool isKDom = false;
	for (int i = 0; i < len; i++)
	{
		if (p[i] >= q[i])
			NumQualifyDim++;
		if (p[i] > q[i])
			numWorstDim++;
		if ((NumQualifyDim >= k) && (numWorstDim > 0))
		{
			isKDom = true;
			break;
		}
	}
	return isKDom;
}

bool kDomByPoints(std::vector<int> &p, std::vector<std::vector<int> > &buffer, int k)
{
	for (std::vector<std::vector<int> >::iterator it = buffer.begin();
	it != buffer.end(); it++)
	{
		if (kDomByPoint(p, *it, k) == true)
			return true;
	}
	return false;
}

std::vector<std::vector<int>> retrieveKDomSkyline(std::vector< std::vector<int> > &buffer, int k)
{
	std::vector<std::vector<int>> result;
	for (std::vector<std::vector<int> >::iterator it = buffer.begin();
	it != buffer.end(); it++)
	{
		bool isDominant = true;
		for (std::vector<std::vector<int> >::iterator itR = result.begin();
		itR != result.end();)
		{
			if (kDomByPoint(*it, *itR, k))
			{
				isDominant = true;
			}
			if (kDomByPoint(*itR, *it, k))
			{
				itR = result.erase(itR);
			}
			else
			{
				itR++;
			}
		}
		if (isDominant)
			result.push_back(*it);
	}

	for (std::vector<std::vector<int> >::iterator it = buffer.begin();
	it != buffer.end(); it++)
	{
		for (std::vector<std::vector<int> >::iterator itR = result.begin();
		itR != result.end();)
		{
			if (kDomByPoint(*itR, *it, k))
			{
				itR = result.erase(itR);
			}
			else
			{
				itR++;
			}
		}
	}
	return result;
}

int getCostCython(std::vector<int> &pUpgrade, std::vector<int> &pOriginal)
{
	int cost = 0;
	unsigned int len = pUpgrade.size();
	for (unsigned int i = 0; i < len; i++)
	{
		cost += (pOriginal[i] - pUpgrade[i]);
	}
	return cost;
}

std::vector<int> getMinCostProductUsingMultipleDim(int currentDIM, std::vector<std::vector<int>>& Skybuffer, std::vector<int> &subspace, std::vector<int>& minCostProduct, std::vector<int> &origionalProduct)
{
	std::vector<int> upgradeProduct(Skybuffer[0].size(), 0);
	std::vector<int> finalMinCostProduct(minCostProduct);
	int minCost = getCostCython(minCostProduct, origionalProduct);

	for (int baseID = 0; baseID < Skybuffer.size() - 1; baseID++)
	{
		upgradeProductMultipleDim(currentDIM, baseID, Skybuffer, subspace, upgradeProduct);
		int aMinCost = getCostCython(upgradeProduct, origionalProduct);
		if (aMinCost < minCost)
		{
			minCost = aMinCost;
			copyProduct(upgradeProduct, finalMinCostProduct);
		}
	}
	return finalMinCostProduct;
}

void upgradeProductMultipleDim(int currentDIM, int basedID, std::vector<std::vector<int>>& Skybuffer, std::vector<int> &subspace, std::vector<int> &upgradeProduct)
{
	copyProduct(Skybuffer[basedID], upgradeProduct);

	for (int k = 0; k < subspace.size(); k++)
	{
		int aDIM = subspace[k];
		if (aDIM == currentDIM)
		{
			upgradeProduct[k] = Skybuffer[basedID + 1][k] - 1;
		}
		else
		{
			upgradeProduct[k] = Skybuffer[basedID][k] - 1;
		}
	}
}

void copyProduct(std::vector<int>& fromProduct, std::vector<int>& toProduct)
{
	for (int i = 0; i < fromProduct.size(); i++)
	{
		toProduct[i] = fromProduct[i];
	}
}
