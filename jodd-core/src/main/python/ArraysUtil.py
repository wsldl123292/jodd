
f = open('ArraysUtil.java', 'w')
f.write('''
// Copyright (c) 2003-2014, Jodd Team (jodd.org). All Rights Reserved.

package jodd.util;

import java.lang.reflect.Array;
import static jodd.util.StringPool.NULL;

/**
 * Array utilities.
 * <b>DO NOT MODIFY: this source is generated.</b>
 */
public class ArraysUtil {

''')

types = ['String', 'byte', 'char', 'short', 'int', 'long', 'float', 'double', 'boolean']
prim_types = ['byte', 'char', 'short', 'int', 'long', 'float', 'double', 'boolean']
big_types = ['Byte', 'Character', 'Short', 'Integer', 'Long', 'Float', 'Double', 'Boolean']
prim_types_safe = ['byte', 'char', 'short', 'int', 'long', 'boolean']

f.write('\n\t// ---------------------------------------------------------------- wrap')
f.write('''

	/**
	 * Wraps elements into an array.
	 */
	public static <T> T[] array(T... elements) {
		return elements;
	}
''')
template = '''
	/**
	 * Wraps elements into an array.
	 */
	public static $T[] $Ts($T... elements) {
		return elements;
	}
'''
for type in prim_types:
	data = template.replace('$T', type)
	f.write(data)

f.write('\n\n\t// ---------------------------------------------------------------- join')
f.write('''

	/**
	 * Joins arrays. Component type is resolved from the array argument.
	 */
	@SuppressWarnings({"unchecked"})
	public static <T> T[] join(T[]... arrays) {
		Class<T> componentType = (Class<T>) arrays.getClass().getComponentType().getComponentType();
		return join(componentType, arrays);
	}

	/**
	 * Joins arrays using provided component type.
	 */
	@SuppressWarnings({"unchecked"})
	public static <T> T[] join(Class<T> componentType, T[][] arrays) {
		if (arrays.length == 1) {
			return arrays[0];
		}
		int length = 0;
		for (T[] array : arrays) {
			length += array.length;
		}
		T[] result = (T[]) Array.newInstance(componentType, length);

		length = 0;
		for (T[] array : arrays) {
			System.arraycopy(array, 0, result, length, array.length);
			length += array.length;
		}
		return result;
	}

''')
template = '''
	/**
	 * Join <code>$T</code> arrays.
	 */
	public static $T[] join($T[]... arrays) {
		if (arrays.length == 0) {
			return new $T[0];
		}
		if (arrays.length == 1) {
			return arrays[0];
		}
		int length = 0;
		for ($T[] array : arrays) {
			length += array.length;
		}
		$T[] result = new $T[length];
		length = 0;
		for ($T[] array : arrays) {
			System.arraycopy(array, 0, result, length, array.length);
			length += array.length;
		}
		return result;
	}
'''
for type in types:
	data = template.replace('$T', type)
	f.write(data)

f.write('\n\n\t// ---------------------------------------------------------------- resize')
f.write('''

	/**
	 * Resizes an array.
	 */
	public static <T> T[] resize(T[] buffer, int newSize) {
		Class<T> componentType = (Class<T>) buffer.getClass().getComponentType();
		T[] temp = (T[]) Array.newInstance(componentType, newSize);
		System.arraycopy(buffer, 0, temp, 0, buffer.length >= newSize ? newSize : buffer.length);
		return temp;
	}

'''
)
template = '''
	/**
	 * Resizes a <code>$T</code> array.
	 */
	public static $T[] resize($T buffer[], int newSize) {
		$T temp[] = new $T[newSize];
		System.arraycopy(buffer, 0, temp, 0, buffer.length >= newSize ? newSize : buffer.length);
		return temp;
	}
'''
for type in types:
	data = template.replace('$T', type)
	f.write(data)


f.write('\n\n\t// ---------------------------------------------------------------- append')
f.write('''

	/**
	 * Appends an element to array.
	 */
	public static <T> T[] append(T[] buffer, T newElement) {
		T[] t = resize(buffer, buffer.length + 1);
		t[buffer.length] = newElement;
		return t;
	}
'''
)
template = '''
	/**
	 * Appends an element to <code>$T</code> array.
	 */
	public static $T[] append($T buffer[], $T newElement) {
		$T[] t = resize(buffer, buffer.length + 1);
		t[buffer.length] = newElement;
		return t;
	}
'''
for type in types:
	data = template.replace('$T', type)
	f.write(data)


f.write('\n\n\t// ---------------------------------------------------------------- remove')
f.write('''

	/**
	 * Removes sub-array.
	 */
	public static <T> T[] remove(T[] buffer, int offset, int length) {
		Class<T> componentType = (Class<T>) buffer.getClass().getComponentType();
		return remove(buffer, offset, length, componentType);
	}

	/**
	 * Removes sub-array.
	 */
	@SuppressWarnings({"unchecked"})
	public static <T> T[] remove(T[] buffer, int offset, int length, Class<T> componentType) {
		int len2 = buffer.length - length;
		T[] temp = (T[]) Array.newInstance(componentType, len2);
		System.arraycopy(buffer, 0, temp, 0, offset);
		System.arraycopy(buffer, offset + length, temp, offset, len2 - offset);
		return temp;
	}
''')
template = '''
	/**
	 * Removes sub-array from <code>$T</code> array.
	 */
	public static $T[] remove($T[] buffer, int offset, int length) {
		int len2 = buffer.length - length;
		$T temp[] = new $T[len2];
		System.arraycopy(buffer, 0, temp, 0, offset);
		System.arraycopy(buffer, offset + length, temp, offset, len2 - offset);
		return temp;
	}
'''
for type in types:
	data = template.replace('$T', type)
	f.write(data)




f.write('\n\n\t// ---------------------------------------------------------------- subarray')
f.write('''

	/**
	 * Returns subarray.
	 */
	public static <T> T[] subarray(T[] buffer, int offset, int length) {
		Class<T> componentType = (Class<T>) buffer.getClass().getComponentType();
		return subarray(buffer, offset, length, componentType);
	}

	/**
	 * Returns subarray.
	 */
	@SuppressWarnings({"unchecked"})
	public static <T> T[] subarray(T[] buffer, int offset, int length, Class<T> componentType) {
		T[] temp = (T[]) Array.newInstance(componentType, length);
		System.arraycopy(buffer, offset, temp, 0, length);
		return temp;
	}
''')
template = '''
	/**
	 * Returns subarray.
	 */
	public static $T[] subarray($T[] buffer, int offset, int length) {
		$T temp[] = new $T[length];
		System.arraycopy(buffer, offset, temp, 0, length);
		return temp;
	}
'''
for type in types:
	data = template.replace('$T', type)
	f.write(data)



f.write('\n\n\t// ---------------------------------------------------------------- insert')
f.write('''

	/**
	 * Inserts one array into another array.
	 */
	public static <T> T[] insert(T[] dest, T[] src, int offset) {
		Class<T> componentType = (Class<T>) dest.getClass().getComponentType();
		return insert(dest, src, offset, componentType);
	}
	/**
	 * Inserts one element into an array.
	 */
	public static <T> T[] insert(T[] dest, T src, int offset) {
		Class<T> componentType = (Class<T>) dest.getClass().getComponentType();
		return insert(dest, src, offset, componentType);
	}

	/**
	 * Inserts one array into another array.
	 */
	@SuppressWarnings({"unchecked"})
	public static <T> T[] insert(T[] dest, T[] src, int offset, Class componentType) {
		T[] temp = (T[]) Array.newInstance(componentType, dest.length + src.length);
		System.arraycopy(dest, 0, temp, 0, offset);
		System.arraycopy(src, 0, temp, offset, src.length);
		System.arraycopy(dest, offset, temp, src.length + offset, dest.length - offset);
		return temp;
	}
	/**
	 * Inserts one element into another array.
	 */
	@SuppressWarnings({"unchecked"})
	public static <T> T[] insert(T[] dest, T src, int offset, Class componentType) {
		T[] temp = (T[]) Array.newInstance(componentType, dest.length + 1);
		System.arraycopy(dest, 0, temp, 0, offset);
		temp[offset] = src;
		System.arraycopy(dest, offset, temp, offset + 1, dest.length - offset);
		return temp;
	}
''')
template = '''
	/**
	 * Inserts one array into another <code>$T</code> array.
	 */
	public static $T[] insert($T[] dest, $T[] src, int offset) {
		$T[] temp = new $T[dest.length + src.length];
		System.arraycopy(dest, 0, temp, 0, offset);
		System.arraycopy(src, 0, temp, offset, src.length);
		System.arraycopy(dest, offset, temp, src.length + offset, dest.length - offset);
		return temp;
	}

	/**
	 * Inserts one element into another <code>$T</code> array.
	 */
	public static $T[] insert($T[] dest, $T src, int offset) {
		$T[] temp = new $T[dest.length + 1];
		System.arraycopy(dest, 0, temp, 0, offset);
		temp[offset] = src;
		System.arraycopy(dest, offset, temp, offset + 1, dest.length - offset);
		return temp;
	}
'''
for type in types:
	data = template.replace('$T', type)
	f.write(data)

f.write('\n\n\t// ---------------------------------------------------------------- insertAt')
f.write('''

	/**
	 * Inserts one array into another at given offset.
	 */
	public static <T> T[] insertAt(T[] dest, T[] src, int offset) {
		Class<T> componentType = (Class<T>) dest.getClass().getComponentType();
		return insertAt(dest, src, offset, componentType);
	}

	/**
	 * Inserts one array into another at given offset.
	 */
	@SuppressWarnings({"unchecked"})
	public static <T> T[] insertAt(T[] dest, T[] src, int offset, Class componentType) {
		T[] temp = (T[]) Array.newInstance(componentType, dest.length + src.length - 1);
		System.arraycopy(dest, 0, temp, 0, offset);
		System.arraycopy(src, 0, temp, offset, src.length);
		System.arraycopy(dest, offset + 1, temp, src.length + offset, dest.length - offset - 1);
		return temp;
	}
''')
template = '''
	/**
	 * Inserts one array into another by replacing specified offset.
	 */
	public static $T[] insertAt($T[] dest, $T[] src, int offset) {
		$T[] temp = new $T[dest.length + src.length - 1];
		System.arraycopy(dest, 0, temp, 0, offset);
		System.arraycopy(src, 0, temp, offset, src.length);
		System.arraycopy(dest, offset + 1, temp, src.length + offset, dest.length - offset - 1);
		return temp;
	}
'''
for type in types:
	data = template.replace('$T', type)
	f.write(data)

f.write('\n\n\t// ---------------------------------------------------------------- convert')
f.write('''

''')

template = '''
	/**
	 * Converts to primitive array.
	 */
	public static $t[] values($T[] array) {
		$t[] dest = new $t[array.length];
		for (int i = 0; i < array.length; i++) {
			$T v = array[i];
			if (v != null) {
				dest[i] = v.$tValue();
			}
		}
		return dest;
	}
	/**
	 * Converts to object array.
	 */
	public static $T[] valuesOf($t[] array) {
		$T[] dest = new $T[array.length];
		for (int i = 0; i < array.length; i++) {
			dest[i] = $T.valueOf(array[i]);
		}
		return dest;
	}

'''
for i in range(len(prim_types)):
	data = template.replace('$t', prim_types[i])
	data = data.replace('$T', big_types[i])
	f.write(data)

f.write('\n\n\t// ---------------------------------------------------------------- indexof')
f.write('''

''')
template = '''
	/**
	 * Finds the first occurrence of an element in an array.
	 */
	public static int indexOf($T[] array, $T value) {
		for (int i = 0; i < array.length; i++) {
			if (array[i] == value) {
				return i;
			}
		}
		return -1;
	}
	/**
	 * Returns <code>true</code> if an array contains given value.
	 */
	public static boolean contains($T[] array, $T value) {
		return indexOf(array, value) != -1;
	}
	/**
	 * Finds the first occurrence of given value in an array from specified given position.
	 */
	public static int indexOf($T[] array, $T value, int startIndex) {
		for (int i = startIndex; i < array.length; i++) {
			if (array[i] == value) {
				return i;
			}
		}
		return -1;
	}
	/**
	 * Finds the first occurrence in an array from specified given position and upto given length.
	 */
	public static int indexOf($T[] array, $T value, int startIndex, int endIndex) {
		for (int i = startIndex; i < endIndex; i++) {
			if (array[i] == value) {
				return i;
			}
		}
		return -1;
	}
'''
for type in prim_types_safe:
	data = template.replace('$T', type)
	f.write(data)

template = '''
	/**
	 * Finds the first occurrence of value in <code>$T</code> array.
	 */
	public static int indexOf($T[] array, $T value) {
		for (int i = 0; i < array.length; i++) {
			if ($B.compare(array[i], value) == 0) {
				return i;
			}
		}
		return -1;
	}
	/**
	 * Returns <code>true</code> if <code>$T</code> array contains given value.
	 */
	public static boolean contains($T[] array, $T value) {
		return indexOf(array, value) != -1;
	}
	/**
	 * Finds the first occurrence of given value in <code>$T</code>
	 * array from specified given position.
	 */
	public static int indexOf($T[] array, $T value, int startIndex) {
		for (int i = startIndex; i < array.length; i++) {
			if ($B.compare(array[i], value) == 0) {
				return i;
			}
		}
		return -1;
	}
	/**
	 * Finds the first occurrence in <code>$T</code> array from specified given position and upto given length.
	 */
	public static int indexOf($T[] array, $T value, int startIndex, int endIndex) {
		for (int i = startIndex; i < endIndex; i++) {
			if ($B.compare(array[i], value) == 0) {
				return i;
			}
		}
		return -1;
	}
'''

data = template.replace('$T', 'float')
data = data.replace('$B', 'Float')
f.write(data)
data = template.replace('$T', 'double')
data = data.replace('$B', 'Double')
f.write(data)

f.write('''
	/**
	 * Finds the first occurrence in an array.
	 */
	public static int indexOf(Object[] array, Object value) {
		for (int i = 0; i < array.length; i++) {
			if (array[i].equals(value)) {
				return i;
			}
		}
		return -1;
	}
	public static boolean contains(Object[] array, Object value) {
		return indexOf(array, value) != -1;
	}

	/**
	 * Finds the first occurrence in an array from specified given position.
	 */
	public static int indexOf(Object[] array, Object value, int startIndex) {
		for (int i = startIndex; i < array.length; i++) {
			if (array[i].equals(value)) {
				return i;
			}
		}
		return -1;
	}
	public static boolean contains(Object[] array, Object value, int startIndex) {
		return indexOf(array, value, startIndex) != -1;
	}


''')


f.write('\n\n\t// ---------------------------------------------------------------- indexof 2')
f.write('''

''')
template = '''
	/**
	 * Finds the first occurrence in an array.
	 */
	public static int indexOf($T[] array, $T[] sub) {
		return indexOf(array, sub, 0, array.length);
	}
	public static boolean contains($T[] array, $T[] sub) {
		return indexOf(array, sub) != -1;
	}


	/**
	 * Finds the first occurrence in an array from specified given position.
	 */
	public static int indexOf($T[] array, $T[] sub, int startIndex) {
		return indexOf(array, sub, startIndex, array.length);
	}

	/**
	 * Finds the first occurrence in an array from specified given position and upto given length.
	 */
	public static int indexOf($T[] array, $T[] sub, int startIndex, int endIndex) {
		int sublen = sub.length;
		if (sublen == 0) {
			return startIndex;
		}
		int total = endIndex - sublen + 1;
		$T c = sub[0];
	mainloop:
		for (int i = startIndex; i < total; i++) {
			if (array[i] != c) {
				continue;
			}
			int j = 1;
			int k = i + 1;
			while (j < sublen) {
				if (sub[j] != array[k]) {
					continue mainloop;
				}
				j++; k++;
			}
			return i;
		}
		return -1;
	}
'''
for type in prim_types_safe:
	data = template.replace('$T', type)
	f.write(data)

template = '''
	/**
	 * Finds the first occurrence in an array.
	 */
	public static int indexOf($T[] array, $T[] sub) {
		return indexOf(array, sub, 0, array.length);
	}
	public static boolean contains($T[] array, $T[] sub) {
		return indexOf(array, sub) != -1;
	}


	/**
	 * Finds the first occurrence in an array from specified given position.
	 */
	public static int indexOf($T[] array, $T[] sub, int startIndex) {
		return indexOf(array, sub, startIndex, array.length);
	}

	/**
	 * Finds the first occurrence in an array from specified given position and upto given length.
	 */
	public static int indexOf($T[] array, $T[] sub, int startIndex, int endIndex) {
		int sublen = sub.length;
		if (sublen == 0) {
			return startIndex;
		}
		int total = endIndex - sublen + 1;
		$T c = sub[0];
	mainloop:
		for (int i = startIndex; i < total; i++) {
			if ($B.compare(array[i], c) != 0) {
				continue;
			}
			int j = 1;
			int k = i + 1;
			while (j < sublen) {
				if ($B.compare(sub[j], array[k]) != 0) {
					continue mainloop;
				}
				j++; k++;
			}
			return i;
		}
		return -1;
	}
'''

data = template.replace('$T', 'float')
data = data.replace('$B', 'Float')
f.write(data)
data = template.replace('$T', 'double')
data = data.replace('$B', 'Double')
f.write(data)


f.write('\n\n\t// ---------------------------------------------------------------- toString')
f.write('''

	/**
	 * Converts an array to string. Elements are separated by comma.
	 * Returned string contains no brackets.
	 */
	public static String toString(Object[] array) {
		if (array == null) {
			return NULL;
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < array.length; i++) {
			if (i != 0) {
				sb.append(',');
			}
			sb.append(array[i]);
		}
		return sb.toString();
	}
'''
)
template = '''
	/**
	 * Converts an array to string. Elements are separated by comma.
	 * Returned string contains no brackets.
	 */
	public static String toString($T[] array) {
		if (array == null) {
			return NULL;
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < array.length; i++) {
			if (i != 0) {
				sb.append(',');
			}
			sb.append(array[i]);
		}
		return sb.toString();
	}
'''
for type in types:
	data = template.replace('$T', type)
	f.write(data)

f.write('''

	/**
	 * Converts an array to string array.
	 */
	public static String[] toStringArray(Object[] array) {
		if (array == null) {
			return null;
		}
		String[] result = new String[array.length];
		for (int i = 0; i < array.length; i++) {
			result[i] = StringUtil.toString(array[i]);
		}
		return result;
	}
'''
)
template = '''
	/**
	 * Converts an array to string array.
	 */
	public static String[] toStringArray($T[] array) {
		if (array == null) {
			return null;
		}
		String[] result = new String[array.length];
		for (int i = 0; i < array.length; i++) {
			result[i] = String.valueOf(array[i]);
		}
		return result;
	}
'''
for type in types:
	data = template.replace('$T', type)
	f.write(data)



f.write('}')
f.close()
