#include <cds/init.h>
#include <cds/gc/hp.h>

int main(int argc, char** argv)
{
   cds::Initialize();
   {
       cds::gc::HP hpGC;
       cds::threading::Manager::attachThread();
   }
   cds::Terminate();
}
