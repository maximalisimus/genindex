#include <QApplication>
#include <QWidget>
#include <QHBoxLayout>
#include <QTreeView>
#include <QDir>
#include <QDirModel>
#include <QString>
#include <iostream>
#include <QFileDialog>

QString version = "1.0";
QString titles = "Tree dir";
QString param;
QString dir_str;
bool _global = false;
int x = 640;
int y = 480;
QString str_x;
QString str_y;

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    for(int i = 0; i < QApplication::arguments().count(); i++)
    {
        param = QApplication::arguments().at(i);
        if(param == "--dir" || param == "-dir" || param == "/d" || param == "-d" | param == "--d")
        {
            dir_str = QApplication::arguments().at(i+1);
            if (not QDir(dir_str).exists()) {

                std::cout<<"The parameters: " << argv[i+1] << " - is not the directory!"<<std::endl;
                return 1;
            } else {
                titles.append(" ");
                titles.append(version);
                titles.append(" - ");
                titles.append(dir_str);
            }
        } else if (param == "-c" | param == "/c" | param == "--c" | param == "--console" | param == "-console") {
            _global = true;
        } else if (param == "-w" | param == "--w" | param == "/w" | param == "-width" | param == "--width") {
            str_x = QApplication::arguments().at(i+1);
            if (str_x.size() != 0) {
                x = str_x.toInt();
            }
        } else if (param == "-h" | param == "--h" | param == "-height" | param == "--height") {
            str_y = QApplication::arguments().at(i+1);
            if (str_y.size() != 0) {
                y = str_y.toInt();
            }
        } else if (param == "-v" | param == "--v" | param == "/v" | param == "-version" | param == "--versioon") {
            std::cout<<"Dir tree."<<std::endl;
            std::cout<<"Version program is: "<<version.toStdString()<<std::endl;
            std::cout<<"About for maximalisimus."<<std::endl;
            exit(0);
        } else if (param == "--help" | param == "-help" | param == "/?" | param == "-?" | param == "?" | param == "/h") {
            std::cout<<"Dir tree. Parameters is:"<<std::endl;
            std::cout<<"-d, --d, -dir, --dir, /d \t\t- directory"<<std::endl;
            std::cout<<"-w, --w, /w, -width, --width \t\t- width to form applaication"<<std::endl;
            std::cout<<"-h, --h, -height, --height \t\t- height fo form application"<<std::endl;
            std::cout<<"-v, --v, /v, -version, --version \t- version"<<std::endl;
            std::cout<<"--help, -help, /?, ?, /h \t\t- help to program"<<std::endl;
            std::cout<<"About for maximalisimus."<<std::endl;
            exit(0);
        }
    }
    if (not _global)
    {
        QWidget *window = new QWidget;
        if (dir_str.size() == 0) {
            dir_str = QFileDialog::getExistingDirectory(0, "Selecto to directory on tree", "");
            titles.append(" ");
            titles.append(version);
            titles.append(" - ");
            titles.append(dir_str);
        }
        QHBoxLayout *layout = new QHBoxLayout;
        window->setWindowTitle(titles);
        window->setFixedSize(x,y);
        QRect rect = window->frameGeometry();
        QPoint point = rect.center();
        window->setGeometry(point.x()/2,point.y()/2,x,y);
        QDirModel *model = new QDirModel();
        model->setReadOnly(false);
        model->setSorting(QDir::DirsFirst | QDir::IgnoreCase | QDir::Name);
        QTreeView *tree = new QTreeView();
        QModelIndex index = model->index(dir_str);
        tree->setModel(model);
        tree->expand(index);
        tree->scrollTo(index);
        tree->setCurrentIndex(index);
        tree->resizeColumnToContents(0);
        //tree->setRowHidden();
        tree->setRootIndex(model->index(dir_str));
        layout->addWidget(tree);
        window->setLayout(layout);
        window->show();
    }
    return app.exec();
}
