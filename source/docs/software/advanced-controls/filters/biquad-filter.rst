# Biquad Filters

The ``BiquadFilter`` class ([Java](https://github.wpilib.org/allwpilib/docs/beta/java/org/wpilib/math/filter/BiquadFilter.html), [C++](https://github.wpilib.org/allwpilib/docs/beta/cpp/classwpi_1_1math_1_1_biquad_filter.html), :external:py:class:`Python <wpimath.BiquadFilter>`) builds sharper low-pass and high-pass filters than the ones on the :doc:`linear-filter` page, and adds two shapes that page does not have: filters that keep only a range of frequencies, and filters that remove one specific frequency.

It does this by chaining together several small filters called [biquads](https://en.wikipedia.org/wiki/Digital_biquad_filter).  You do not have to know how a biquad works to use the class.  The factory methods below design the whole chain for you from a few numbers you choose.

## When Do I Want This?

Usually you don't.  For smoothing a noisy sensor, :ref:`LinearFilter.singlePoleIIR() <docs/software/advanced-controls/filters/linear-filter:singlePoleIIR>` is still the right first thing to try.  It is easy to tune, it is cheap to run, and it is good enough for most mechanisms on most robots.

Reach for ``BiquadFilter`` when a simple filter isn't cutting it:

- **You need a sharper cutoff.**  Every low-pass filter has a cutoff frequency: slow changes below it pass through, and fast changes above it get removed.  But the change isn't sudden.  A simple filter fades out gradually, so noise a little bit above the cutoff still leaks through.  A biquad filter can make that fade much steeper.
- **You need to remove one specific frequency.**  If a mechanism vibrates at a known rate, a *notch* filter cuts out that one frequency and leaves the rest of your signal alone.
- **You need to keep only a range of frequencies.**  ``LinearFilter`` can't do this at all.

There is also a practical reason the class works in small chunks instead of one big calculation.  Sharp filters need a lot of math, and doing it all at once makes rounding errors pile up until the output goes haywire.  Splitting the work into a chain of small filters keeps the numbers well behaved.

## Some Words You'll Need

Filter documentation uses a handful of terms that are worth getting straight before the next section.

- The **passband** is the range of frequencies you want to keep.  The **stopband** is the range you want to remove.
- **Attenuation** means how much a frequency gets shrunk.  It is measured in [decibels](https://en.wikipedia.org/wiki/Decibel) (dB).  Every 20 dB means ten times smaller, so 20 dB of attenuation leaves a tenth of the signal, 40 dB leaves a hundredth, and 60 dB leaves a thousandth.
- **Ripple** means the filter doesn't treat every frequency in a band exactly the same.  Instead of one flat level, the response wobbles slightly up and down as the frequency changes.  A little ripple is usually harmless, and some filter designs trade a bit of it for a sharper cutoff.
- **Order** is how many biquads get chained together.  A higher order gives a sharper cutoff, but also more :ref:`phase lag <docs/software/advanced-controls/filters/introduction:Phase Lag>`, meaning the filtered value takes longer to catch up when the real value changes.  Use the lowest order that does the job.

## Choosing a Filter Family

There are four classic ways to design a filter.  They all do the same job, and they differ in what they give up to get a sharper cutoff.

.. list-table:: Filter Families
   :header-rows: 1

   * - Family
     - Ripple in the Passband?
     - Ripple in the Stopband?
     - Sharpness
     - Use It When
   * - [Butterworth](https://en.wikipedia.org/wiki/Butterworth_filter)
     - No
     - No
     - Least sharp
     - You don't have a specific requirement.  Start here.
   * - [Chebyshev I](https://en.wikipedia.org/wiki/Chebyshev_filter)
     - Yes
     - No
     - Sharper
     - You need a sharper cutoff and don't mind a small wobble in the frequencies you're keeping.
   * - [Chebyshev II](https://en.wikipedia.org/wiki/Chebyshev_filter)
     - No
     - Yes
     - Sharper
     - You need a sharper cutoff, and the frequencies you're keeping have to come through evenly.
   * - [Elliptic](https://en.wikipedia.org/wiki/Elliptic_filter)
     - Yes
     - Yes
     - Sharpest
     - You need the sharpest cutoff you can get and can live with a wobble in both bands.

If you aren't sure, use Butterworth.  It is the safe choice, and if it isn't sharp enough you can raise the order before switching families.

## Creating a BiquadFilter

.. note:: Because filters have "memory", each input stream requires its own filter object.  Do *not* attempt to use the same filter object for multiple input streams.

Each of the four families has a factory method.  They all take a ``Kind``, which is the shape of the filter, plus the order, the sample rate, and one or two frequencies.  ``Kind`` has four values:

- ``LowPass`` keeps frequencies below the cutoff and removes the ones above it.  This is the one you want for smoothing a noisy sensor.
- ``HighPass`` does the opposite, keeping frequencies above the cutoff.
- ``BandPass`` keeps only the frequencies between two cutoffs, and removes everything else.
- ``BandStop`` removes the frequencies between two cutoffs, and keeps everything else.

.. warning:: Each factory has two versions, and they are not interchangeable.  The version taking a single ``cutoff`` works only with ``LowPass`` and ``HighPass``.  The version taking a ``lowCutoff`` and a ``highCutoff`` works only with ``BandPass`` and ``BandStop``.  Mixing them up throws ``IllegalArgumentException`` in Java, ``std::invalid_argument`` in C++, and ``ValueError`` in Python.

.. note:: In Python the ``Kind`` values are spelled ``BiquadFilter.Kind.LOW_PASS``, ``HIGH_PASS``, ``BAND_PASS``, and ``BAND_STOP``, following Python naming conventions.  The C++ factories take ``wpi::units::hertz_t`` instead of ``double`` for every frequency.

The last two factories, ``notch`` and ``movingAverage``, each have one fixed design, so they take neither a ``Kind`` nor an order.

### Butterworth

The ``butterworth`` factory treats every frequency in a band evenly, with no ripple anywhere.  Its cutoff is the least sharp of the four families, which is a fine trade for most robot code.  Start here.

.. tab-set-code::

   ```java
   // Creates a 4th-order Butterworth low-pass filter
   // Sample rate is 50 Hz, the standard main loop rate
   // Cutoff frequency is 5 Hz
   BiquadFilter filter = BiquadFilter.butterworth(BiquadFilter.Kind.LowPass, 4, 50.0, 5.0);
   ```

   ```c++
   // Creates a 4th-order Butterworth low-pass filter
   // Sample rate is 50 Hz, the standard main loop rate
   // Cutoff frequency is 5 Hz
   wpi::math::BiquadFilter filter = wpi::math::BiquadFilter::Butterworth(
       wpi::math::BiquadFilter::Kind::LowPass, 4, 50_Hz, 5_Hz);
   ```

   ```python
   from wpimath import BiquadFilter
   # Creates a 4th-order Butterworth low-pass filter
   # Sample rate is 50 Hz, the standard main loop rate
   # Cutoff frequency is 5 Hz
   filter = BiquadFilter.butterworth(BiquadFilter.Kind.LOW_PASS, 4, 50.0, 5.0)
   ```

For a ``BandPass`` or ``BandStop`` filter, use the version that takes two frequencies instead.

.. tab-set-code::

   ```java
   // Creates a Butterworth band-pass filter that keeps 5 Hz to 15 Hz
   BiquadFilter filter = BiquadFilter.butterworth(BiquadFilter.Kind.BandPass, 2, 50.0, 5.0, 15.0);
   ```

   ```c++
   // Creates a Butterworth band-pass filter that keeps 5 Hz to 15 Hz
   wpi::math::BiquadFilter filter = wpi::math::BiquadFilter::Butterworth(
       wpi::math::BiquadFilter::Kind::BandPass, 2, 50_Hz, 5_Hz, 15_Hz);
   ```

   ```python
   from wpimath import BiquadFilter
   # Creates a Butterworth band-pass filter that keeps 5 Hz to 15 Hz
   filter = BiquadFilter.butterworth(BiquadFilter.Kind.BAND_PASS, 2, 50.0, 5.0, 15.0)
   ```

### Chebyshev Type I

The ``chebyshevI`` factory gives a sharper cutoff than Butterworth by allowing some ripple in the passband.  The extra ``rippleDb`` argument is how big that wobble is allowed to be, in decibels.  It has to be greater than zero, and anything from about 0.1 dB to 3 dB is normal.

.. tab-set-code::

   ```java
   // Creates a 4th-order Chebyshev type-I low-pass filter
   // Cutoff frequency is 5 Hz, allowing 1 dB of ripple
   BiquadFilter filter = BiquadFilter.chebyshevI(BiquadFilter.Kind.LowPass, 4, 50.0, 5.0, 1.0);
   ```

   ```c++
   // Creates a 4th-order Chebyshev type-I low-pass filter
   // Cutoff frequency is 5 Hz, allowing 1 dB of ripple
   wpi::math::BiquadFilter filter = wpi::math::BiquadFilter::ChebyshevI(
       wpi::math::BiquadFilter::Kind::LowPass, 4, 50_Hz, 5_Hz, 1.0);
   ```

   ```python
   from wpimath import BiquadFilter
   # Creates a 4th-order Chebyshev type-I low-pass filter
   # Cutoff frequency is 5 Hz, allowing 1 dB of ripple
   filter = BiquadFilter.chebyshev_i(BiquadFilter.Kind.LOW_PASS, 4, 50.0, 5.0, 1.0)
   ```

There is also a version taking a ``lowCutoff`` and a ``highCutoff`` for ``BandPass`` and ``BandStop``, with ``rippleDb`` last.

### Chebyshev Type II

The ``chebyshevII`` factory is the mirror image of ``chebyshevI``.  The passband stays even, and the ripple goes in the stopband instead.  Its extra ``stopAttenDb`` argument is how far down the stopband has to be pushed, in decibels.  It has to be greater than zero, and anything from about 20 dB to 80 dB is normal.

One thing to watch: for this family the ``cutoff`` you pass is where the stopband *starts*, not where the passband ends.  Frequencies below it come through, and frequencies above it are down by at least ``stopAttenDb``.

.. tab-set-code::

   ```java
   // Creates a 4th-order Chebyshev type-II low-pass filter
   // The stopband starts at 5 Hz, and everything above it is at least 40 dB down
   BiquadFilter filter = BiquadFilter.chebyshevII(BiquadFilter.Kind.LowPass, 4, 50.0, 5.0, 40.0);
   ```

   ```c++
   // Creates a 4th-order Chebyshev type-II low-pass filter
   // The stopband starts at 5 Hz, and everything above it is at least 40 dB down
   wpi::math::BiquadFilter filter = wpi::math::BiquadFilter::ChebyshevII(
       wpi::math::BiquadFilter::Kind::LowPass, 4, 50_Hz, 5_Hz, 40.0);
   ```

   ```python
   from wpimath import BiquadFilter
   # Creates a 4th-order Chebyshev type-II low-pass filter
   # The stopband starts at 5 Hz, and everything above it is at least 40 dB down
   filter = BiquadFilter.chebyshev_ii(BiquadFilter.Kind.LOW_PASS, 4, 50.0, 5.0, 40.0)
   ```

There is also a version taking a ``lowCutoff`` and a ``highCutoff`` for ``BandPass`` and ``BandStop``, with ``stopAttenDb`` last.

### Elliptic

The ``elliptic`` factory allows ripple in both bands, and in exchange gives the sharpest cutoff you can get at a given order.  It takes both ``rippleDb`` and ``stopAttenDb``, and ``stopAttenDb`` has to be bigger than ``rippleDb``.

.. tab-set-code::

   ```java
   // Creates a 4th-order elliptic low-pass filter
   // Cutoff frequency is 5 Hz, allowing 1 dB of ripple
   // and pushing the stopband at least 40 dB down
   BiquadFilter filter = BiquadFilter.elliptic(BiquadFilter.Kind.LowPass, 4, 50.0, 5.0, 1.0, 40.0);
   ```

   ```c++
   // Creates a 4th-order elliptic low-pass filter
   // Cutoff frequency is 5 Hz, allowing 1 dB of ripple
   // and pushing the stopband at least 40 dB down
   wpi::math::BiquadFilter filter = wpi::math::BiquadFilter::Elliptic(
       wpi::math::BiquadFilter::Kind::LowPass, 4, 50_Hz, 5_Hz, 1.0, 40.0);
   ```

   ```python
   from wpimath import BiquadFilter
   # Creates a 4th-order elliptic low-pass filter
   # Cutoff frequency is 5 Hz, allowing 1 dB of ripple
   # and pushing the stopband at least 40 dB down
   filter = BiquadFilter.elliptic(BiquadFilter.Kind.LOW_PASS, 4, 50.0, 5.0, 1.0, 40.0)
   ```

There is also a version taking a ``lowCutoff`` and a ``highCutoff`` for ``BandPass`` and ``BandStop``, with ``rippleDb`` and ``stopAttenDb`` last.

### Notch

The ``notch`` factory removes one specific frequency and leaves everything else alone.  Use it when something on your robot vibrates at a rate you can measure, such as a mechanical resonance or a wheel wobble at a steady speed.  It takes no ``Kind`` and no order.

The ``qualityFactor`` argument, usually written Q, sets how narrow the notch is.  A higher Q removes a narrower slice of frequencies.  If you know the frequency you are trying to kill exactly, use a high Q.  If it drifts around a bit, use a lower one so the notch is wide enough to catch it.  There is more on this at [Q factor](https://en.wikipedia.org/wiki/Q_factor) on Wikipedia.

.. tab-set-code::

   ```java
   // Creates a notch filter centered on 10 Hz
   // Quality factor of 10. Higher values give a narrower notch
   BiquadFilter filter = BiquadFilter.notch(50.0, 10.0, 10.0);
   ```

   ```c++
   // Creates a notch filter centered on 10 Hz
   // Quality factor of 10. Higher values give a narrower notch
   wpi::math::BiquadFilter filter = wpi::math::BiquadFilter::Notch(50_Hz, 10_Hz, 10.0);
   ```

   ```python
   from wpimath import BiquadFilter
   # Creates a notch filter centered on 10 Hz
   # Quality factor of 10. Higher values give a narrower notch
   filter = BiquadFilter.notch(50.0, 10.0, 10.0)
   ```

### Moving Average

The ``movingAverage`` factory averages the last few samples together.  It takes only the number of ``taps``, which is how many samples go into the average.

This is the same filter that :ref:`LinearFilter.movingAverage() <docs/software/advanced-controls/filters/linear-filter:movingAverage>` gives you, and ``LinearFilter`` is the easier way to get one.  The version here exists so a moving average can be built into a longer chain alongside other filters.

.. tab-set-code::

   ```java
   // Creates a flat moving average over the last 5 samples
   BiquadFilter filter = BiquadFilter.movingAverage(5);
   ```

   ```c++
   // Creates a flat moving average over the last 5 samples
   wpi::math::BiquadFilter filter = wpi::math::BiquadFilter::MovingAverage(5);
   ```

   ```python
   from wpimath import BiquadFilter
   # Creates a flat moving average over the last 5 samples
   filter = BiquadFilter.moving_average(5)
   ```

## Using the Filter

.. note:: Unlike ``LinearFilter``, the C++ ``BiquadFilter`` class is not templated.  It takes and returns ``double``.

Using the filter is the same as any other WPILib filter.  Call ``calculate()`` once per loop with your newest reading, and it hands back the filtered value:

.. tab-set-code::

   ```java
   // Calculates the next value of the output
   filter.calculate(input);
   ```

   ```c++
   // Calculates the next value of the output
   filter.Calculate(input);
   ```

   ```python
   # Calculates the next value of the output
   filter.calculate(input)
   ```

Three other methods are worth knowing.  ``reset()`` wipes the filter's memory back to zero, which is what you want after a gap in ``calculate()`` calls.  ``reset(value)`` instead fills the memory as if the filter had been fed ``value`` over and over, so it starts out already settled instead of ramping up from zero.  That is handy when you know the reading in advance, like resetting an arm's filter to the arm's current position at the start of a match.  ``lastValue()`` gives you the most recent output again without running the filter forward.

.. tab-set-code::

   ```java
   // Clears the filter state
   filter.reset();
   // Seeds the filter as if it had been fed 5.0 for a long time
   filter.reset(5.0);
   // Returns the most recent output
   double output = filter.lastValue();
   ```

   ```c++
   // Clears the filter state
   filter.Reset();
   // Seeds the filter as if it had been fed 5.0 for a long time
   filter.Reset(5.0);
   // Returns the most recent output
   double output = filter.LastValue();
   ```

   ```python
   # Clears the filter state
   filter.reset()
   # Seeds the filter as if it had been fed 5.0 for a long time
   filter.reset(5.0)
   # Returns the most recent output
   output = filter.last_value()
   ```

## Sample Rate Matters

.. warning:: A filter is built around the rate you said you would call it at.  ``calculate()`` has to run on a steady, known period, and the ``sampleRate`` you gave the factory has to match it.  If it doesn't, every frequency in your design shifts, and nothing warns you.

The robot main loop runs every 20 ms, which is 50 times per second, so the sample rate is 50 Hz.  If you call ``calculate()`` from ``robotPeriodic()`` or from a subsystem's ``periodic()`` method, 50 is the number to pass.  If you run the filter somewhere else, such as in a notifier or over data logged at a different rate, use that rate instead.

The sample rate also limits which cutoff frequencies make sense.  Every cutoff has to be below half the sample rate, a limit called the [Nyquist frequency](https://en.wikipedia.org/wiki/Nyquist_frequency).  On the 50 Hz main loop that means cutoffs below 25 Hz.  The reason is simple enough: you can't measure a wiggle that happens faster than you're looking.

The factories check their arguments and will throw ``IllegalArgumentException`` in Java, ``std::invalid_argument`` in C++, or ``ValueError`` in Python if the order is below 1, the sample rate isn't positive, a cutoff is out of range, or two cutoffs are given in the wrong order.

## Advanced: Building a Filter by Hand

If you already have the numbers for a filter, usually because a filter design tool worked them out for you, you can build a ``BiquadFilter`` from them directly instead of calling a factory.  A ``Section`` holds the five numbers that describe one biquad, called ``b0``, ``b1``, ``b2``, ``a1``, and ``a2``.  Pass the sections in the order they should run.

.. tab-set-code::

   ```java
   // A 4th-order Butterworth low-pass, 50 Hz sample rate, 5 Hz cutoff,
   // written out directly as two sections
   BiquadFilter filter =
       new BiquadFilter(
           new BiquadFilter.Section(0.00482434, 0.00964869, 0.00482434, -1.04859958, 0.29614036),
           new BiquadFilter.Section(1.0, 2.0, 1.0, -1.32091343, 0.63273879));
   ```

   ```c++
   // A 4th-order Butterworth low-pass, 50 Hz sample rate, 5 Hz cutoff,
   // written out directly as two sections
   wpi::math::BiquadFilter filter{
       wpi::math::BiquadFilter::Section{0.00482434, 0.00964869, 0.00482434, -1.04859958,
                                        0.29614036},
       wpi::math::BiquadFilter::Section{1.0, 2.0, 1.0, -1.32091343, 0.63273879}};
   ```

   ```python
   from wpimath import BiquadFilter
   # A 4th-order Butterworth low-pass, 50 Hz sample rate, 5 Hz cutoff,
   # written out directly as two sections
   filter = BiquadFilter(
       [
           BiquadFilter.Section(0.00482434, 0.00964869, 0.00482434, -1.04859958, 0.29614036),
           BiquadFilter.Section(1.0, 2.0, 1.0, -1.32091343, 0.63273879),
       ]
   )
   ```

A filter needs at least one section, and an empty one is rejected.  Going the other way, ``numSections()`` tells you how many sections a filter has and ``sections()`` hands back a copy of them, which is useful for logging a filter you designed elsewhere.
