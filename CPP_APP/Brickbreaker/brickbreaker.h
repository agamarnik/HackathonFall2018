#ifndef BRICKBREAKER_H
#define BRICKBREAKER_H

#include <QMainWindow>

namespace Ui {
class BrickBreaker;
}

class BrickBreaker : public QMainWindow
{
    Q_OBJECT

public:
    explicit BrickBreaker(QWidget *parent = 0);
    ~BrickBreaker();

private:
    Ui::BrickBreaker *ui;
};

#endif // BRICKBREAKER_H
