#include "brickbreaker.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    BrickBreaker w;
    w.show();

    return a.exec();
}
