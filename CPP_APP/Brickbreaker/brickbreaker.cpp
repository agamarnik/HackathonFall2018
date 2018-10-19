#include "brickbreaker.h"
#include "ui_brickbreaker.h"

BrickBreaker::BrickBreaker(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::BrickBreaker)
{
    ui->setupUi(this);
}

BrickBreaker::~BrickBreaker()
{
    delete ui;
}
