#include "StringContainer.h"

int main()
{
	StringContainer sc("hello, abuba");
	int (* Search)(char) = &StringContainer::StaticCharCount;
	int n = Search('k');
	int (StringContainer:: *Search2)(char) = &StringContainer::InstanceCharCount;
	n = (sc.*Search2)('a');
	return 0;
}
