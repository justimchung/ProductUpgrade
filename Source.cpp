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