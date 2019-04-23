#include <vector>
#include <string>


#ifndef INDEX_INDEX_ITEM_H
#define INDEX_INDEX_ITEM_H

class IndexItem
{
public:
    std::vector<int> Friends;
    std::vector<float> Embedding;
    std::string Key;
    int Id;

    IndexItem(const std::string& key, const std::vector<float>& embedding)
            : Key(key), Embedding(embedding), Friends(), Id()
    {}

    double GetSquareDistance(const std::vector<float>& otherEmbedding) {
        double result = 0;
        for (int i = 0; i < Embedding.size(); ++i) {
            double temp = Embedding[i] - otherEmbedding[i];
            result += temp * temp;
        }
        return result;
    }
};

#endif //INDEX_INDEX_ITEM_H
