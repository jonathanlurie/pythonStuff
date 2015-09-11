# SplineCurveHandler has the purpose of mimicing the behavior of
# Adobe Photoshop curves. They are cubic splines with a 0 second derivative
# at there extremity. This is achived by creating a straight segment at the
# begining en at the end of the curve. Or rather before the begining and
# after the end.



from scipy.interpolate import interp1d
import numpy as np


class SplineCurveHandler:

    # series of data over X axis
    _xSeries = None

    # series of data over y axis
    _ySeries = None

    # extented series for x.
    # contains 2 additional values : 1 before and 1 after _xSeries
    # to make the first and last point of _xSeries having a 0 second derivative.
    _xSeriesExtended = None

    # extented series for y.
    # contains 2 additional values : 1 before and 1 after _ySeries
    # to make the first and last point of _ySeries having a 0 second derivative.
    _ySeriesExtended = None

    # scipy function result of interpolation
    _fInterpol = None

    def __init__(self):
        None

    # extends the original series by adding two points at the head and two points
    # at the tail, thus creating segment-like (not curvy) endings. The purpose
    # is to have a null (0) second derivative at the extremities
    def _extendSeries(self):
        # creating segment at the extremities
        xBefore = self._xSeries[0] - (self._xSeries[1] - self._xSeries[0])
        yBefore = self._ySeries[0] - (self._ySeries[1] - self._ySeries[0])
        xAfter = self._xSeries[-1] + (self._xSeries[-1] - self._xSeries[-2])
        yAfter = self._ySeries[-1] + (self._ySeries[-1] - self._ySeries[-2])

        self._xSeriesExtended = list(self._xSeries)
        self._ySeriesExtended = list(self._ySeries)

        self._xSeriesExtended.insert(0, xBefore)
        self._ySeriesExtended.insert(0, yBefore)

        self._xSeriesExtended.append(xAfter)
        self._ySeriesExtended.append(yAfter)

        # second points

        xBefore = self._xSeriesExtended[0] - (self._xSeriesExtended[1] - self._xSeriesExtended[0])
        yBefore = self._ySeriesExtended[0] - (self._ySeriesExtended[1] - self._ySeriesExtended[0])
        xAfter = self._xSeriesExtended[-1] + (self._xSeriesExtended[-1] - self._xSeriesExtended[-2])
        yAfter = self._ySeriesExtended[-1] + (self._ySeriesExtended[-1] - self._ySeriesExtended[-2])

        self._xSeriesExtended.insert(0, xBefore)
        self._ySeriesExtended.insert(0, yBefore)

        self._xSeriesExtended.append(xAfter)
        self._ySeriesExtended.append(yAfter)



    def setData(self, xSeries, ySeries):

        if(not isinstance(xSeries, list) or not isinstance(ySeries, list) ):
            raise TypeError('xSeries and ySeries must be of type list.')

        if(len(xSeries) != len(ySeries)):
            raise ValueError('xSeries and ySeries must have the same length.')

        # set the attributes
        self._xSeries = xSeries
        self._ySeries = ySeries

        # add tail and head to get Null second derivative at extemities
        self._extendSeries()

        # directly run the interpolation
        self._fInterpol = interp1d( np.array(self._xSeriesExtended), np.asarray(self._ySeriesExtended), kind='cubic')


    # return an interpolated data, using cubic splines.
    # if xValue is array-typed, it will return an array-typed result
    # if xValue is a scalar, it will return a scalar result
    def getInterpolatedData(self, xValue):
        return self._fInterpol(xValue)


    # show the curve using matplotlib
    def show(self):

        try:
            import matplotlib.pyplot as plt
            xnew = np.linspace(0, 255, 100)
            plt.plot(self._xSeries, self._ySeries,'o', xnew, self._fInterpol(xnew),'-')
            plt.legend(['Data','Cubic'], loc='best')
            plt.show()
        except ImportError:
            print("Matplotlib was not found, impossible to display curve.")



# testing
if __name__ == '__main__':

    # original data, must be the same length
    xData = [0, 64, 191, 255]
    yData = [0, 48, 208, 255]

    # instanciation
    sch = SplineCurveHandler()

    # setting the input data
    sch.setData(xData, yData)

    # printing a value, result of the cubic interpolation
    print sch.getInterpolatedData(10)

    # showing the curve using Matplotlib, optional (ImportError handled)
    sch.show()
